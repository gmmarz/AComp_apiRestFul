from flask import Flask

app = Flask(__name__)

@app.route('/') #/info é considerado o primeiro endpoint
def root():
    return 'Hello world flask' 

@app.route('/info') #/info é considerado o primeiro endpoint
def info():
    return 'Api Funcionando Normalmente' 


if __name__ == '__main__':
    app.run(debug=True)