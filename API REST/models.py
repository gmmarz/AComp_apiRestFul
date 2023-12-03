from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()

class Livro(db.Model):
    id: int = Column(Integer,primary_key=True,autoincrement=True)
    nome: str = Column(String(255), nullable=False)
    autor: str = Column(String(255), nullable=False)
    isbn: str = Column(String(255), nullable=False)
    
    def to_json(self):
        return{'id': self.id,'nome':self.nome,'autor':self.autor,'isbn': self.isbn}
    