from django.db.backends.base.base import BaseDatabaseWrapper

from spreadbase.db import Database
from spreadbase.schema import DatabaseSchemaEditor
from spreadbase.client import DatabaseClient
from spreadbase.creation import DatabaseCreation
from spreadbase.features import DatabaseFeatures
from spreadbase.introspection import DatabaseIntrospection
from spreadbase.operations import DatabaseOperations


class DatabaseWrapper(BaseDatabaseWrapper):
    Database = Database
    SchemaEditorClass = DatabaseSchemaEditor
    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    def get_connection_params(self):
        return {
            'client_secret': self.settings_dict['CLIENT_SECRET'],
            'file_name': self.settings_dict['FILE_NAME']
        }

    def get_new_connection(self, conn_params):
        return Database.connect(conn_params)

    def init_connection_state(self):
        pass

    def create_cursor(self, name=None):
        return self.connection.get_cursor()

    def _set_autocommit(self, autocommit):
        pass
