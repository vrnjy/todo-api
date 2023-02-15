from db import db

class TodoModel(db.Model): # type: ignore
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80), unique=False, nullable=False)
    check = db.Column(db.Integer, nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return{
            'id': self.id,
            'content': self.content,
            'check': self.check
        }
    
