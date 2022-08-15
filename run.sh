set -a
. .env
set +a

if [ "$APP_ENV" = "development" ]; then
  nodemon src/__main__.py
elif [ "$APP_ENV" = "production" ]; then
  pdm export >requirements.txt
  docker compose build && docker compose up -d
else
  echo "\$APP_ENV must be development/production"
fi
