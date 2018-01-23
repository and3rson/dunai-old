import re
import sqlparse


class Query(object):
    def __init__(self, sql):
        self.statement = sqlparse.parse(sql)[0]

    def execute(self, cursor):
        handler = Query.HANDLERS[self.statement.get_type()]
        return handler(self, cursor)

    def _load_worksheet(self, worksheet):
        rows = worksheet.get_all_values()
        print('ROWS:', rows)
        try:
            schema = rows.pop(0)
        except IndexError:
            return []

        return [
            dict(zip(schema, row))
            for row
            in rows
        ]

    def _select(self, cursor):
        self._load_worksheet(cursor.gfile.worksheet(
            self.statement.get_name()
        ))
        # self.statement.

    def _insert(self, cursor):
        pass

    def _create(self, cursor):
        index, keyword = self.statement.token_next(0)
        if keyword.value == 'TABLE':
            cursor.gfile.add_worksheet(
                self.statement.get_name(),
                rows=1000,
                cols=32
            )
        elif keyword.value == 'COLUMN':
            s

    HANDLERS = {
        'SELECT': _select,
        'INSERT': _insert,
        # 'UPDATE': _update,
        # 'DELETE': _delete,
        'CREATE': _create,
        # 'ALTER': _alter,
        # 'DROP': _drop
    }
