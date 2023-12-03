from flask import Flask
from http import HTTPStatus
from models import db,Livro

#Configurações da aplicação
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.json.sort_keys = False

with app.app_context():
    db.init_app(app)
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)