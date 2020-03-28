from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from flask import Response
from flask import request
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from. import models

db = SQLAlchemy(app)

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