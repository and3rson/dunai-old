from django.db.backends.base.introspection import (
    BaseDatabaseIntrospection,
    TableInfo
)


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor):
        return [
            TableInfo(sheet.title, 't')
            for sheet
            in cursor.gfile.worksheets()
        ]

    def get_table_description(self, cursor):
        a
