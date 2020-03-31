from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask import Response
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from flask_login import login_required, logout_user, current_user, login_user
from. import models

db = SQLAlchemy(app)

@app.route('/login', methods=['POST'])
def handeLogin():
    data = request.json
    username=data['username']
    password=data['password']
    print("login attempt - ", username )
    try:
        found = db.session.query(models.Account).\
            filter(models.Account.username==username).\
            one()
        if found.check_password(password=password):
            login_user(found)
            response = Response()
            response.status_code = 200
        return response

    except MultipleResultsFound:
        response = Response()
        response.status_code = 500
        response.set_data("Could not login, multiple accounts found")
        return response
    except NoResultFound:
        response = Response()
        response.status_code = 404
        response.set_data("Could not login, no account found")
        return response
    except Exception as e:
        print("general exception", e)
        response = Response()
        response.status_code = 400
        response.set_data("Could not login")
        return response

@app.route('/new-account', methods=['POST'])
def handeNewAccount():
    data = request.json
    username=data['username']
    password=data['password']
    print("New Account attempt " + username)
    try:
        found = db.session.query(models.Account).\
            filter(models.Account.username==username).\
            first()
        if found is None:
            account = models.Account(
                username=data['username'],
                password=data['password']
            )
            db.session.add(account)
            db.session.commit()
            login_user(account)
            return "ok"
        else:
            response = Response()
            response.status_code = 409
            response.set_data("Username " + username + " already exists" )
            return response
    except Exception as e:
        response = Response()
        response.status_code = 500
        response.set_data("Could not save to DB " + str(e))
        return response