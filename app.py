from flask import Flask
from prisma import Prisma, register
from routes.todo import todo_blueprint

db = Prisma()
db.connect()
register(db)

app = Flask(__name__)

app.register_blueprint(todo_blueprint, url_prefix='/todo')


# @app.route('/', methods=['GET'])
# def index():
#     return {
#         "💥": "👊"
#     }


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
