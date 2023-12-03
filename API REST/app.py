from flask import Flask
from http import HTTPStatus
from models import db,Livro

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livraria.db'
app.json.sort_keys = False #Desabilita a auto ordenação

@app.route('/') #/info é considerado o primeiro endpoint
def root():
    return 'Hello world flask' 

@app.route('/info') #/info é considerado o primeiro endpoint
def info():
    return 'Api Funcionando Normalmente' 

with app.app_context():
    db.init_app(app) #Comando para iniciar o banco
    db.create_all() #Comando para criar as tabelas.


if __name__ == '__main__':
    app.run(debug=True)