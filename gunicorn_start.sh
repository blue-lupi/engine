python manage.py migrate

# Create the default admin user on startup after applying migrations.
python manage.py autocreate_user

python -m gunicorn francy.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:80