web: gunicorn to_do_list.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
