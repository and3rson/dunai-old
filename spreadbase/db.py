from weakref import proxy

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from spreadbase.log import logger
from spreadbase.query import Query


class Database(object):
    class DataError(Exception):
        pass
    class OperationalError(Exception):
        pass
    class IntegrityError(Exception):
        pass
    class InternalError(Exception):
        pass
    class ProgrammingError(Exception):
        pass
    class NotSupportedError(Exception):
        pass
    class DatabaseError(Exception):
        pass
    class InterfaceError(Exception):
        pass
    class Error(Exception):
        pass

    @classmethod
    def connect(cls, conn_params):
        connection = Connection(conn_params)
        connection.connect()
        return connection


class Cursor(object):
    """
    A virtual cursor to comply to Django DB backends architecture.
    """
    def __init__(self, connection, gfile):
        self.connection = proxy(connection)
        self.gfile = gfile

        self.query = None
        self.result = None

    def execute(self, query, params=None):
        logger.info('Query: %s', query)
        self.query = Query(query)
        self.result = self.query.execute(self)

    def fetchmany(self, *args, **kwargs):
        assert self.query, 'No query executed'

        if self.result is None:
            return None

        result = self.result
        self.result = None
        return result

    def fetchone(self, *args, **kwargs):
        assert self.query, 'No query executed'

        if self.result is None:
            return None

        try:
            return self.result.pop(0)
        except IndexError:
            return None

    def close(self):
        """
        Do nothing - no closing needed.
        """
        pass


class Connection(object):
    """
    Google Docs connection class.
    """
    def __init__(self, conn_params):
        self.conn_params = conn_params

    def connect(self):
        logger.debug('Parsing client_secret.json')
        scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            self.conn_params['client_secret'],
            scope
        )
        logger.debug('Authorizing in Google Docs')
        self.client = gspread.authorize(self.creds)
        logger.debug('Opening spreadsheet')
        self.gfile = self.client.open(self.conn_params['file_name'])
        logger.debug('Connected')

    def get_cursor(self):
        return Cursor(self, self.gfile)

    def close(self):
        pass

