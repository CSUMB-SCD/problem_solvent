# Running the App
## Run Configuration is Necessary
You must use the run configuration called RunDjango because the environment variable is required
Then you can use the commands below
** The VM will not work anymore with the new postgresql db

#Run these commands in the terminal
    python manage.py runserver 0.0.0.0:8080

# other commands you may want

## run unittests
python manage.py test

## if static files aren't loading
python manage.py collectstatic

## to add a new app
python manage.py startapp your_app_name

## setup the apps (creates db entries and gets everything ready)
python manage.py migrate

## start postgres server
if something on port 5432 isn't working
sudo service postgresql start

## start redis service
if something on port 6397 isn't working
sudo service redis-server start

## demo user for Heroku
username: test_user
password: soluti0n (there is a zero instead of O)
