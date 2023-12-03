from flask import Flask, request
from http import HTTPStatus
from models import db,Livro

#Boas praticas para desenvolvimento, e para um clean code
#Não colocar retornos ou utilizar valores numericos em hardcodes. 
#Ideal é criar constantes para o codico ser mais compreensível.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livraria.db'
app.json.sort_keys = False #Desabilita a auto ordenação

@app.route('/') #/info é considerado o primeiro endpoint
def root():
    return 'Hello world flask' 

@app.route('/info') #/info é considerado o primeiro endpoint
def info():
    return 'Api Funcionando Normalmente' 

@app.route('/livro/', methods = ['GET'])
def listar_livros():
    livros = db.session.query(Livro).all()
    if len(livros) == 0:
        return ('',HTTPStatus.NO_CONTENT)
    return ([livro.to_json() for livro in livros], HTTPStatus.OK)

@app.route('/livro/', methods = ['POST'])
def cadastrar_livro():
    livro: dict = request.get_json()
    
    if livro.get('nome') is None:
        return ({'message':'O campo nome é obrigatório'}, HTTPStatus.BAD_REQUEST)

    if livro.get('autor') is None:
        return ({'message':'O campo autor é obrigatório'}, HTTPStatus.BAD_REQUEST)

    if livro.get('isbn') is None:
        return ({'message':'O campo isbn é obrigatório'}, HTTPStatus.BAD_REQUEST)
    
    livro: Livro = Livro(nome = livro.get('nome'), autor = livro.get('autor'), isbn = livro.get('isbn'))
    db.session.add(livro)
    db.session.commit()
    
    return ({'message':'Livro cadastrado com sucesso'}, HTTPStatus.CREATED)    

with app.app_context():
    db.init_app(app) #Comando para iniciar o banco
    db.create_all() #Comando para criar as tabelas.


if __name__ == '__main__':
    app.run(debug=True)