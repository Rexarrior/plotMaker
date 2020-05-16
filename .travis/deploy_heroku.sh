#!/bin/sh
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
docker login -u $DOCKER_USER --password $DOCKER_PASS registry.heroku.com
heroku container:push web --app $HEROKU_APP_NAME