# Running the App

#Run these commands in the terminal
    cd problem_solvent
    pipenv shell
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
