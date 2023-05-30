from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas #per le figure
from matplotlib.figure import Figure

indirizzo_statale = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/csvRecuperoFlask_cvs/ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021.csv',sep=";")

app = Flask(__name__)   #variabile che identifica il sito web

@app.route('/', methods=['GET'])  #sono tutte le possibili richieste del utente
def home():
    
    return render_template("indexHome.html")
####################################1##############################
@app.route('es1',  methods = ['POST', 'GET'])  #sono tutte le possibili richieste del utente
def es1():

    return render_template("indexHome.html",indirizzo_statale=indirizzo_statale.to_html())


@app.route('/solEs1', methods = ['POST', 'GET'])  #sono tutte le possibili richieste del utente
def solEs1():
    scuola = request.args.get('scuola')
    dfscuola = indirizzo_statale[(indirizzo_statale.DenominazioneScuola == scuola) & (indirizzo_statale.DenominazioneScuola == scuola)].sort_values(by='date')

    return render_template("soluzione1.html",dfscuola = dfscuola.to_html())

##################################################################2#########################################
@app.route('/es2', methods=['GET'])  #sono tutte le possibili richieste del utente
def es2():
    percorsoScolastico = indirizzo_statale[~indirizzo_statale['PERCORSO'].str.contains('\|')]['PERCORSO'].to_list()
    percorsoScolastico = list(set(percorsoScolastico))
    return render_template("index1.html")

@app.route('/solEs2', methods = ['POST', 'GET'])  #sono tutte le possibili richieste del utente
def solEs2():


    return render_template("soluzione1.html",dfInQurtieri = dfInQurtieri.to_html())



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)    #fà partire il programma
