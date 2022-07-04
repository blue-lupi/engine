python manage.py migrate

# Create the default admin user on startup after applying migrations.
#  python manage.py autocreate_user

# Heroku handles worker spawning and port binding for us.
python -m gunicorn francy.asgi:application -k uvicorn.workers.UvicornWorker
