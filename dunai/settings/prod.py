from .common import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    '127.0.0.1:8000',
    'dunai',
    'dunai:8000',
    'dun.ai',
    'dun.ai:8000',
    'www.dun.ai',
    'www.dun.ai:8000'
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
