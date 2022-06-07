# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template

app = Flask(__name__)

dogs = [
    {'id': 1, 'nome': 'Thor', 'raça': 'Yorkshire', 'status': 'adoção'},
    {'id': 2, 'nome': 'Lola', 'raça': 'Shitzu', 'status': 'adoção'},
    {'id': 3, 'nome': 'Joaquim', 'raça': 'Buldog frances', 'status': 'adoção'}

]


@app.route('/')
def home():
    return render_template('home.html', dogs=dogs) 

app.run(debug=True)





# CLIENTE -- SERVIDOR
# Navegador -- AWS (Flask)

# Client -> REQUEST (MENSAGEM HTTP) -> Server 
# Server -> RESPONSE (MENSAGEM HTTP) -> CLIENTE

# HTTP (HyperText Transfer Protocol)
# HTML (HyperText Markup Language)

# Mensagem HTTP:
# Header
# Body
# METHOD (GET, POST), Métodos suportados pelos navegadores.
# GET -> DADOS PELA URL
# POST -> OCULTO OS DADOS (NAO MOSTRA URL)

# METHOD (API = GET, POST, PUT, DELETE, PATCH, OPTIONS)   

# REST    
# POST    (C)REATE
# GET     (R)EAD
# PUT     (U)PDATE
# PATH    (U)PDATE PARCIAL
# DELETE  (D)ELETE 
