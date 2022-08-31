web: daphne chat.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
heroku config:set DJANGO_SETTINGS_MODULE=chat.settings --account personal
worker: python manage.py runworker -v2
