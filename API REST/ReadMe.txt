Aula compartilha de API RestFull.

dontpad - infinitybh-restapi
baixar insomnia - é um cliente de requisição.

thunder client do VS code, também faz a mesma função do insomnia

no browser - apertar F12 para abrir a ferramenta do desenvolvedor.

Projeto do davi - to-do-app-hwx0.onrender.com/home

Anotações

API - Aplication Program Interface
    - Um programa que permite controlar uma funcionalidade complexa com uma interface mais simples.
Internet funciona atraves de uma protocolo de comunicação:
WWW - World wide web
    -URL é uma localização de uma determinada funcionalidade na internet.
    -HTML - Hyper text Markup language 
    -HTTP - Hyper text transfer protocol
    
Protocolo HTTP
    Padrão de comunicação entre dois sistemas computacionais. 
    Realizado no esquema de requisição e resposta. 

    resposta 404 - Not found - tem haver com o endereço.
    resposta 400 - Bad request.

O que é uma API REST:
Rest - representational state transfer
Rest é uma arquitetura que dita um conjunto de regras e boas praticas que surjerem como 
um serviço web deve disponibilizar seus endpoints e os estados das entidades que ela tiver trabalhando.

metodos http:
GET - para fazer uma consulta
POST - para inserir um novo dado
PUT - Para alterar um dado existente, passando todas as informações do que será alterado
DELETE - Para excluir um dado existente
PATCH - Para alterar um dado existente, mas passando apenas o que será alterado.

Configuração do enviroment do insomnia;
{
	"task_api": "https://to-do-app-hwx0.onrender.com",
	"localhost": "127.0.0.1:5000"
}

Principios Rest
Quando uma Api aplica todas as restrições da arquitetura REST, dizemos que ela é uma API RESTful.


RECOMENDADO SEMPRE UTILIZAR UM AMBIENTE VIRTUAL DO PYTHON
comandos - 
python -m venv 'nome ambiente'
exemplo -python -m venv .venv

para ativar o ambiente
.(nome do ambiente)/Scripts/activate
exemplo:
.venv/Scripts/activate 


