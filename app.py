from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/new-account', methods=['POST'])
def handeNewAccount():
    data = request.json
    print(data['username'], data['password'])
    return "ok"

if __name__ == '__main__':
    app.run()