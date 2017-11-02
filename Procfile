web: gunicorn problem_solvent.wsgi --log-file -
web: daphne problem_solvent.asgi:channel_layer --port $PORT --bind 0.0.0.0
worker: python manage.py runworker -v2
