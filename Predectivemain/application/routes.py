from application import app
from flask import render_template, url_for
import pandas as pd 
import json
import plotly
import plotly.express as px


@app.route("/")
def index():

    df = pd.read_csv('F:/canspirit/plant monitoring/PdM_machines.csv')
    fig1 = px.scatter(df, x='machineID', y='model', color='age') 
    fig1.update_traces(mode='markers+lines')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('index.html', graph1JSON = graph1JSON )