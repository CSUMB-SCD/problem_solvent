# Homework 5 Questions
Team Members: 

* Nigel Hardy: Worked on getting the environment working with Python/Django/Websockets/Redis/Postgres and setup the backend.

* Meya Gorbea: Worked on the front end displaying messages and the user count/list.

* Manuel Gonzalez: Researched Django Channels

## Our Strategy
We have a Cloud9 workspace, so we can easily work on something and avoid merge conflicts. We also split up the tasks into backend, frontend, and deployment. 

## What are known problems, if any, with your project?
If the app crashes, then it won't delete connected users. Should probably reset that table in the db on startup.

## How would you improve it if you had more time?
Integrate it into our application's theme better. Right now it is on its own stylistically. It also asks for your name using a prompt, which is not elegant.

Admin account: prob_solv
Password: 41SOLUTION**

# Running the App
1. Run the RunDjango Run Configuration
2. python manage.py runserver 0:8080
3. If port 5432 is giving error run: sudo service postgresql start
4. If port 6379 is giving error run: sudo service redis-server start
5. Repeat step 2 after starting Redis and Postgres

Go to website: https://problem-solvent-nigelhardy.c9users.io:8080
Theme Website: https://html5up.net/alpha
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

username: first
password: soluti0n
## backup db
## This will save it properly
python manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --indent 4 > data.json

## restore db
python manage.py loaddata db.json


