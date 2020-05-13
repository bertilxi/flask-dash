from flask import Flask
from flask import render_template
import plotly.express as px
from plotly.offline import plot

app = Flask(__name__)

@app.route('/')
def home():
    fig =px.scatter(x=range(10), y=range(10))
    graph = plot(fig, output_type='div')
    return render_template('index.html', graph=graph)

@app.route('/graph1')
def graph1():
    fig =px.scatter(x=range(20), y=range(20))
    graph = plot(fig, output_type='div')
    return render_template('index.html', graph=graph)

@app.route('/graph2')
def graph2():
    fig =px.scatter(x=range(30), y=range(30))
    graph = plot(fig, output_type='div')
    return render_template('index.html', graph=graph)