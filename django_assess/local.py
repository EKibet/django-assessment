from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('SECRET_KEY',default='5(-34b%k6dq@2+ary-=#!wd8^rcsak3zko7&y5*7ilppgap72!')
ALLOWED_HOSTS = ['*']