from flask import Blueprint, request
from prisma import Prisma

todo_blueprint = Blueprint('todo', __name__)
prisma = Prisma()


@todo_blueprint.route('/', methods=["GET"])
def list_todos():
    todos = prisma().todo.find_many()
    return todos


@todo_blueprint.route('/', methods=["POST"])
def create_todo():
    data = request.get_json()
    if data is None:
        return

    content = data.get('content')

    if content is None:
        return {"Error": "Please provide content."}
    todo = prisma().todo.create(data={
        'content': content,
    })

    return todo.dict()


@todo_blueprint.route('/<int:id>', methods=["GET"])
def get_todo(id):
    if id is None:
        return {"Error": "Please privide id."}

    todo = prisma().todo.find_unique(where={
        'id': id
    })
    if todo is None:
        return {"Error": "Todo doesn't exist."}
    return todo.dict()


@todo_blueprint.route('/<int:id>', methods=["PUT"])
def update_todo(id):
    if id is None:
        return {"Error": "Please privide id."}

    data = request.json
    if data is None:
        return

    content = data.get('content')

    if content is None:
        return {"Error": "Please provide content."}

    todo = prisma().todo.update(where={'id': id}, data={'content': content})

    return todo.dict()


@todo_blueprint.route('/<int:id>', methods=["DELETE"])
def delete_todo(id):
    if id is None:
        return {"Error": "Please provide id."}
    todo = prisma().todo.delete(where={'id': id})

    if todo is None:
        return {'Error': "Todo doesn't exist."}

    return todo.dict()
