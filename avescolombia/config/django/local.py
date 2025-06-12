from .base import *

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['0.0.0.0', 'localhost', '127.0.0.1', '192.168.0.12', 'cc23-2800-484-127a-a200-4cd1-2050-b915-72a.ngrok-free.app'])


INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]