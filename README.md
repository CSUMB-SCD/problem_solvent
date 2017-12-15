## CircleCI Status [![CircleCI](https://circleci.com/gh/CSUMB-SCD/problem_solvent.svg?style=svg&circle-token=9bbddaaa4310633b363982d784075154253134f2)](https://circleci.com/gh/CSUMB-SCD/problem_solvent) 
[CircleCI Link](https://circleci.com/gh/CSUMB-SCD/problem_solvent)

## Wiki
See our [Wiki](https://github.com/CSUMB-SCD/problem_solvent/wiki) to learn about our process.

## Our Strategy
We have a Cloud9 workspace, so we can easily work on something and avoid merge conflicts. We also split up the tasks into backend, frontend, and deployment. Django also allows for separating the project into 'applications,' so we can each work on independent aspects of the project at the same time.
### Github commits don't reflect our contributions exactly because many were pushed from Cloud9. 

### Known Issues
Heroku by default uses an ephemeral file system and does not store the uploaded photos. It works perfect temporarily and works on cloud 9.

We would need to implement buckets on an AWS S3 server and only having a 3 person group limited out capabilities. It would have been interesting to learn, but we did not have time.

# Running the App
1. Make sure you have setup the proper environment variables (PostgreSQL, Redis, Google Auth)
2. python manage.py runserver 0:8080
3. If port 5432 is giving error run: sudo service postgresql start
4. If port 6379 is giving error run: sudo service redis-server start

Go to website: [Heroku Application Link](https://problem-solvent.herokuapp.com)

## Other useful Django commands

### Run unittests
python manage.py test

### When static files aren't loading
python manage.py collectstatic

### Add a new app
python manage.py startapp your_app_name

### Setup the apps/db (creates db entries and gets everything ready)
python manage.py makemigrations
python manage.py migrate

### Start postgres server
if something on port 5432 isn't working
sudo service postgresql start

### Start redis service
if something on port 6397 isn't working
sudo service redis-server start

## Backup DB
### This will save it properly
python manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --exclude admin.logentry --indent 4 > data.json

### Run with test db for checking with throw away db
python manage.py testserver data_test.json --addrport 0:8080

### Restore db
python manage.py loaddata db.json