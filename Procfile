web: gunicorn my_first_django_project.wsgi --log-file -
release: python manage.py migrate
web: run-program waitress-serve --port=$PORT settings.wsgi:application