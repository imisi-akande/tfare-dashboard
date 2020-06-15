from tfareapp import app
from flask import render_template
from wrangling_scripts.wrangling import data_wrangling

data = data_wrangling()

# print(data)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')