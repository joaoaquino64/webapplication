# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template
import csv

app = Flask(__name__)


dogs = [
    {'id': 1, 'nome': 'Thor', 'raça': 'Yorkshire', 'status': 'adoção'},
    {'id': 2, 'nome': 'Lola', 'raça': 'Shitzu', 'status': 'adoção'},
    {'id': 3, 'nome': 'Joaquim', 'raça': 'Buldog francês', 'status': 'adoção'}
]

with open('dogs.csv', 'wt') as file_out:
    escritor = csv.writer(file_out)
    escritor.writeows(dogs)

@app.route('/')
def home():
    return render_template('home.html', dogs=dogs) 

app.run(debug=True)