source .env/bin/activate
django-admin startproject main
python manage.py runserver
python manage.py startapp Backgammon
python manage.py collectstatic --noinput --clear # Si les statics ne s'appliquent plus, vider le cache du navigateur en plus