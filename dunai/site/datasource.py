import os
from time import time
from threading import Thread

import gspread
from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials


class CachedDocument(object):
    def __init__(self, table, data=None):
        self.table = table
        self.data = None
        self.last_update = None
        self.update(data)

    def update(self, data):
        self.data = data
        self.last_update = time()

    def get_is_valid(self, ttl):
        return self.last_update + ttl > time()


class DataSource(object):
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            os.path.join(settings.BASE_DIR, 'client_secret.json'),
            scope
        )
        client = gspread.authorize(creds)

        # Знаходимо файл за ім'ям та відкриваємо першу таблицю
        self.document = client.open("Database")

        self.cached_documents = {}

    def get_table(self, table, ttl=10):
        if table in self.cached_documents:
            print('Returning cache')
            document = self.cached_documents[table]

            if not document.get_is_valid(ttl):
                print('Spawning update')
                document.update(document.data)
                Thread(target=self._update_document, args=(document,)).start()
        else:
            print('Creating new')
            document = CachedDocument(table)
            document.update(self._get_table(table))
            self.cached_documents[table] = document

        return document.data

    def _update_document(self, document):
        document.update(self._get_table(document.table))

    def _get_table(self, table):
        sheet = self.document.worksheet(table)
        return sheet.get_all_records()


ds = DataSource()
