# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)


dogs = [{'id': uuid4(), 'Nome': 'Caramelo', 'Raça': 'Vira Lata', 'Cor': 'Caramelo', 'Idade': '1 ano', 'Status': 'Pronto para adoção'}]

with open('dogs.csv', 'w') as file_out:
    escritor = csv.DictWriter(file_out, ['id', 'Nome', 'Raça', 'Cor', 'Idade', 'Status'])
    escritor.writeheader()
    escritor.writerows(dogs)

@app.route('/')
def home():
    return render_template('home.html', dogs=dogs) 

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['Nome']
    raça = request.form['Raça']
    cor = request.form['Cor']
    idade = request.form['Idade']
    status = request.form['Status']
    dogs.append({'id': uuid4(), 'Nome': nome, 'Raça': raça, 'Cor': cor, 'Idade': idade, 'Status': status})
    return redirect('/')

app.run(debug=True)