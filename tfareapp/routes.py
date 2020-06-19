from tfareapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangling import return_page_one_figures, return_page_two_figures

@app.route('/')
@app.route('/index')
def index():

    figures = return_page_one_figures()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON)

@app.route('/page-two')
def page_two():

    figures_page_two = return_page_two_figures()
    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures_page_two)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures_page_two, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('others.html',
                           ids=ids,
                           figuresJSON=figuresJSON)