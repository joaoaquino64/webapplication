# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template
import csv

app = Flask(__name__)


dogs = [
    {'id': 1, 'nome': 'Thor', 'raça': 'Yorkshire', 'status': 'pronto para adoção'},
    {'id': 2, 'nome': 'Lola', 'raça': 'Shitzu', 'status': 'necessita vacinação'},
    {'id': 3, 'nome': 'Joaquim', 'raça': 'Buldog francês', 'status': 'necessita cuidados especiais'}
]

with open('dogs.csv', 'wt') as file_out:
    escritor = csv.writer(file_out)
    escritor.writerows(dogs)

@app.route('/')
def home():
    return render_template('home.html', dogs=dogs) 

app.run(debug=True)