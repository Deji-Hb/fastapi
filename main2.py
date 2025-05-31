# primary key is a unique identifier for a column like id or email that can't occur more than once
# good practice in sql is to capitalize sql specific words but leave yours in lower
# instead of communicating with the database directly using sql queries we can use regular standard codes
# with the help of an ORM (Object-Relational Mapping). It has no relationship with fastapi
# sqlalchemy is one of the popular ORM'S
# sql cannot talk to a database but needs a driver for the package you're using eg psycopg2 for fastapi
#using models to define our tables
#a signature is a combination of the header, payload and a secret password in the token. 
#only on the backend can you access the secret password not even the frontend should have access to it
#a query parameter is after the question mark sign after a website domain name to get specific info from the website
#to access an environment variable
import os
path = os.getenv("MY_DB_URL")
print(path)
#alembic heads shows the latest head
#do not run alembic revision on our production server. You only run it on the development serve
#on the production server we do a git push
#NGINX is a high performance web server that can ast as a proxy and is used to perform ssl termination