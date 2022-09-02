# dj_model

We are using django models for setting up and maintaining database.

Why?
1. we know django well enough for this.
2. Django orm is not bad. We don't want to read another orm.
3. We can track migrations.
4. Python is best as a scripting language. It's time we give it not more than what it deserves.


### Setup

1. `brew install pyenv`

2. `pyenv install 3.8.0`

3. `pyenv virtualenv 3.8.0 lhenv`

4. `pyenv activate lhenv`

5. `pip install -r backend/requirements.txt`

5.a install PostgreSQL, visit the link here – https://www.postgresql.org/download/

5.b sudo -u postgres psql 

5.c in psql console run following:-
    5.c.z > CREATE ROLE root;
    5.c.y > ALTER USER root WITH PASSWORD 'rootpass';
    5.c.x > CREATE DATABASE lhdb;
    
6. `python manage.py migrate`

7. `python manage.py runserver`


------------------------------------------------------------------
###### folly
django admin - admin and pass

