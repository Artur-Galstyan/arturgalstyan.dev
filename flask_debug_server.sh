export FLASK_APP=main
export FLASK_ENV=development
(trap 'kill 0' SIGINT; npm run watch-css & python -m flask run )