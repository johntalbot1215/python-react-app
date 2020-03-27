import os
from flask import Flask
from flask import request
from flask import Response
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

app = Flask(__name__)

#TODO put in config.py
#also use python-dotenv


def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import models
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/login', methods=['POST'])
def handeLogin():
    data = request.json
    print("login", data['username'], data['password'])
    try:
        found = db.session.query(models.Account).\
            filter(models.Account.username==data["username"]).\
            filter(models.Account.password==data["password"]).\
            one()
        response = Response()
        response.error_code = 200
        response.set_data("id=" + str(found.id))
        return response

    except MultipleResultsFound:
        response = Response()
        response.error_code = 500
        response.set_data("Could not login, multiple accounts found")
        return response
    except NoResultFound:
        response = Response()
        response.error_code = 404
        response.set_data("Could not login, no account found")
        return response
    except Exception as e:
        print("general exception", e)
        response = Response()
        response.error_code = 400
        response.set_data("Could not login")
        return response

@app.route('/new-account', methods=['POST'])
def handeNewAccount():
    data = request.json
    print(data['username'], data['password'])
    try:
        account = models.Account(
            username=data['username'],
            password=data['password']
        )
        db.session.add(account)
        db.session.commit()
    except:
        response = Response()
        response.error_code = 400
        response.set_data("Could not save to DB")
        return response
    return "ok"

if __name__ == '__main__':
    app.run()
