web:    gunicorn --pythonpath meow --workers=2 meow.wsgi --log-file -
worker: export PYTHONPATH=meow && celery -A meow worker -l info --concurrency=1
clock:  export PYTHONPATH=meow && celery -A meow beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler