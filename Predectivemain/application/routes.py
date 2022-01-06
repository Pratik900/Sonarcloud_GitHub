from application import app
from flask import render_template, url_for
import pandas as pd 
import json
import plotly
import plotly.express as px


@app.route("/")
def index():
#graph 1 
    df = pd.read_csv('F:/canspirit/plant monitoring/PdM_machines.csv')
    fig1 = px.scatter(df, x='machineID', y='model', color='age') 
    fig1.update_traces(mode='markers+lines')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

#graph 2
    df = pd.read_csv('F:/canspirit/plant monitoring/PdM_failures.csv')
    fig2 = px.scatter(df, x = 'machineID', y = 'failure' ,title='Failures')
    #fig2 = px.box(df, x = 'failure', y = 'machineID' )
    #fig2.update_traces(quartilemethod="inclusive")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

#graph 3
    df = pd.read_csv('F:/canspirit/plant monitoring/PdM_telemetry.csv')
    fig3 = px.box(df, x="machineID", y="volt")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', graph1JSON = graph1JSON , graph2JSON = graph2JSON , graph3JSON = graph3JSON )