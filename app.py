from db import db
from flask_restful import Api
from werkzeug.exceptions import HTTPException, default_exceptions
from flask import Flask, jsonify
from todo.resource import TodoList, Todo
from dotenv import load_dotenv
import os


app = Flask(__name__)

# register error handlers.
@app.errorhandler(Exception) # type: ignore
def handle_error(err):
    code = 500
    if isinstance(err, HTTPException):
        code = err.code
    return jsonify(error=str(err)), code

for excp in default_exceptions:
    app.register_error_handler(excp, handle_error)

# set app configuration
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['BUNDLE_ERRORS'] = os.getenv('BUNDLE_ERRORS')


# initialize db and resful entry point with flask app
db.init_app(app)
api = Api(app)
api.prefix = '/api'


# @app.before_first_request
# def create_tables():
#     db.drop_all()
#     db.create_all()


# TODO
# register todo resource
api.add_resource(TodoList, "/todo")
api.add_resource(Todo, "/todo/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)