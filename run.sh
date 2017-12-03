#!/bin/sh
sudo service postgresql start       #wouldn't this make it better to being with to prevent any errors from happening? correct me if I'm wrong or if there is a specific
sudo service redis-server start     # reaon why shouldn't run it at every instance
pipenv shell python manage.py runserver 0.0.0.0:8080    #wouldnt this be better since we wouldnt have to manually type pyhton manage.py.... ? 
                                                    