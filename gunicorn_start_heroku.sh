python manage.py migrate

# Create the default admin user on startup after applying migrations.
#  python manage.py autocreate_user

# Heroku handles worker spawning and port binding for us.
# python -m gunicorn francy.asgi:application -k uvicorn.workers.UvicornWorker

uwsgi \
    --socket=127.0.0.1:$PORT \
    --buffer-size=32768 \
    --env UWSGI_WSGI_FILE=esite/wsgi_production.py \
    --processes=4 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum \
    --http-auto-chunked \
    --http-keepalive
