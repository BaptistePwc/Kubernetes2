from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.engine import create_engine
from kubernetes import client, config
import os

config.load_incluster_config()
v1 = client.CoreV1Api()

mysql_url = os.environ.get('MYSQL_HOST')
secret = v1.read_namespaced_secret(name='my-secret', namespace='default')
mysql_password = secret.data.get('mysql-password').decode('utf-8')
mysql_user = 'root'
database_name = 'Main'

# recreating the URL connection
connection_url = 'mysql+pymysql://{user}:{password}@{url}/{database}?charset=utf8mb4'.format(
    user=mysql_user,
    password=mysql_password,
    url=mysql_url,
    database=database_name
)

# creating a FastAPI server
server = FastAPI(title='User API')

# creating a connection to the database
mysql_engine = create_engine(connection_url)


# creating a User class
class User(BaseModel):
    user_id: int = 0
    username: str = 'daniel'
    email: str = 'daniel@datascientest.com'


@server.get('/status')
async def get_status():
    """Returns 1"""
    return 1


@server.get('/users')
async def get_users():
    with mysql_engine.connect() as connection:
        results = connection.execute('SELECT * FROM Users;')

    results = [
        User(
            user_id=i[0],
            username=i[1],
            email=i[2]
        ) for i in results.fetchall()]
    return results


@server.get('/users/{user_id:int}', response_model=User)
async def get_user(user_id):
    with mysql_engine.connect() as connection:
        results = connection.execute(
            'SELECT * FROM Users WHERE Users.id = {};'.format(user_id))

    results = [
        User(
            user_id=i[0],
            username=i[1],
            email=i[2]
        ) for i in results.fetchall()]

    if len(results) == 0:
        raise HTTPException(
            status_code=404,
            detail='Unknown User ID')
    else:
        return results[0]
