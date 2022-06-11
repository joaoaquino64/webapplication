# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)


dogs = []

with open('dogs.csv', 'r') as file_in:
    l = csv.DictReader(file_in)
    for dog in l:
        dogs.append(dict(dog))

def salvar_csv():
    with open('dogs.csv', 'w') as file_out:
        e = csv.DictWriter(file_out, ['id', 'Nome', 'Raça', 'Cor', 'Idade', 'Status'])
        e.writeheader()
        e.writerows(dogs)

@app.route('/')
def home():
    salvar_csv()
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

@app.route('/edit/<id>')
def edit(id):
    for dog in dogs:
        id_string = str(dog['id'])
        if id_string == id: 
            return render_template('edit.html', dog=dog)

@app.route('/update/<id>', methods=['POST'])
def update(id):
    for dog in dogs:
        id_string = str(dog['id'])
        if id == id_string:
            id_dog_editado = dog['id']

    nome = request.form['Nome']
    raça = request.form['Raça']
    cor = request.form['Cor']
    idade = request.form['Idade']
    status = request.form['Status']
    dogs[dogs.index(dog)] = {'id': id_dog_editado, 'Nome': nome, 'Raça': raça, 'Cor': cor, 'Idade': idade, 'Status': status}
    return redirect('/')

@app.route('/adoption/<id>')
def delete(id):
    for dog in dogs:
        id_string = str(dog['id'])
        if id_string == id:
            del dogs[dogs.index(dog)]
            return render_template('adoptioned.html')


app.run(debug=True)