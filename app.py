# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4
import csv

app = Flask(__name__)


dogs = [{'id': uuid4(), 'Nome': 'Joaquim', 'Raça': 'Lulu da Pomerânia', 'Cor': 'Castanho', 'Idade': '6 meses', 'Status do cão': 'Pronto para adoção'}]

with open('dogs.csv', 'w') as file_out:
    escritor = csv.DictWriter(file_out, ['id', 'Nome', 'Raça', 'Cor', 'Idade', 'Status do cão'])
    escritor.writeheader()
    escritor.writerows(dogs)

@app.route('/')
def home():
    return render_template('home.html', dogs=dogs) 

@app.route('/add')
def add():
    return render_template('add.html')


app.run(debug=True)