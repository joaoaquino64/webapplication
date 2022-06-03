# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html') 

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
