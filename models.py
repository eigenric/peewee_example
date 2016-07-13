from peewee import *
from playhouse.db_url import connect

from config import data

# mysql_db = MySQLDatabase('library', user='pwaqo', passwd='pass') Local

mysql_db = connect("mysql://{user}:{passwd}@{host}:3306/{db}".format(**data))

class BaseModel(Model):

	class Meta:
		database = mysql_db

class Book(BaseModel):

    author = CharField()
    title = TextField()

if __name__ == '__main__':

	Book.create_table()
