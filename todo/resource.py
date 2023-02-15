from flask import request
from flask_restful import Resource
from todo.model import TodoModel
from sqlalchemy.exc import SQLAlchemyError


class Todo(Resource):
    
    # Retrieve, update or delete a todo. 
    
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

        if content == '':
            return {'messange': 'Cannot have nothing todo.'}, 400
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

        try:
            todo.save_to_db()
        except SQLAlchemyError:
            return {"message": "An error occurred while toggeling the todo. :("}, 500
        
        return todo.json(), 200




class TodoList(Resource):
    
    # List all todos and create new ones.
    
    def get(self):
        todos = [todo.json() for todo in TodoModel.find_all()]

        return {'todos': todos}, 200
    
    def post(self):
        content = request.form['content']
        todo = TodoModel(content=content)

        try:
            todo.save_to_db()
        except SQLAlchemyError:
            return {'error': 'An error occured while adding todo :('}, 500
        
        return todo.json(), 201
    
    
        