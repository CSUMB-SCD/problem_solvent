# Running the App
1. Run the RunDjango Run Configuration
2. python manage.py runserver 0:8080
3. If port 5432 is giving error run: sudo service postgresql start
4. If port 6379 is giving error run: sudo service redis-server start
5. Repeat step 2 after starting Redis and Postgres

Go to website: https://problem-solvent-nigelhardy.c9users.io:8080

## Run Configuration is Necessary
You must use the run configuration called RunDjango because the environment variable is required

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
