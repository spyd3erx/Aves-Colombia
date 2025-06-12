from .base import *
from avescolombia.config.env import BASE_DIR, env

DEBUG = env.bool('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
