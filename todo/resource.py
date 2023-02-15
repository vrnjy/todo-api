from flask import request
from flask_restful import Resource, reqparse
from todo.model import TodoModel
from sqlalchemy.exc import SQLAlchemyError


class Todo(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=str,
                        required=True,
                        help="Need a todo id.",
                        )
    
    def get(self, id):
        todo = TodoModel.find_by_id(id)
        if todo:
            return todo.json(), 200
        return {'message': 'Todo not found.'}, 404
        
    def delete(self, id):
        todo = TodoModel.find_by_id(id)

        if not todo:
            return {'message': 'Could not delete todo.'}, 404

        try:
            todo.delete_from_db()
        except SQLAlchemyError:
            return {"message": "An error occurred while deleting the todo. :("}, 500

        return todo.json(), 200
    
    def put(self, id):
        content = request.form['content']

        todo = TodoModel.find_by_id(id)

        if not todo:
            return {'message': 'Could not update.'}, 404

        todo.content = content
        
        try:
            todo.save_to_db()
        except SQLAlchemyError:
            return {"message": "An error occurred while updating the todo. :("}, 500

        return todo.json(), 201

    def patch(self, id):

        todo = TodoModel.find_by_id(id)
        if not todo:
            return {'message': 'Could not toggle.'}, 404
        
        todo.check = not todo.check

class TodoList(Resource):
    def get(self):
        todos = [todo.json() for todo in TodoModel.find_all()]

        return {'todos': todos}, 200
    
    def post(self):
        content = request.form['content']
        check = request.form['check']
        todo = TodoModel(content=content, check=check)

        try:
            todo.save_to_db()
        except SQLAlchemyError:
            return {'error': 'An error occured while adding todo :('}, 500
        
        return todo.json(), 201
    
    
        