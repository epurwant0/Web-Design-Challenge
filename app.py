import csv
from flask import Flask, render_template, url_for
import os
app = Flask(__name__)

RESOURCES = os.path.join('static', 'Resources')
app.config['UPLOAD_FOLDER'] = RESOURCES
logo = os.path.join(app.config['UPLOAD_FOLDER'], 'assets', 'images', 'Brand_Logo.png')
fig1 = os.path.join(app.config['UPLOAD_FOLDER'], 'assets', 'images', 'Fig1.png')
fig2 = os.path.join(app.config['UPLOAD_FOLDER'], 'assets', 'images',  'Fig2.png')
fig3 = os.path.join(app.config['UPLOAD_FOLDER'], 'assets', 'images',  'Fig3.png')
fig4 = os.path.join(app.config['UPLOAD_FOLDER'], 'assets', 'images',  'Fig4.png')

@app.route('/')
def index():
    return render_template('index.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/comparisons')
def comparisons():
    return render_template('comparisons.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/max-temp')
def maxTemp():
    return render_template('max-temp.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/humidity')
def humidity():
    return render_template('humidity.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/cloudiness')
def cloudiness():
    return render_template('cloudiness.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/wind-speed')
def windSpeed():
    return render_template('wind-speed.html', logo = logo, fig1 = fig1, fig2 = fig2, fig3 = fig3, fig4 = fig4)

@app.route('/data.html')
def data():
    latPath = open('./static/Resources/cities.csv')
    reader = csv.reader(latPath)
    latData = []
    for row in reader:
        latData.append(row)
    return render_template('data.html', logo = logo, latData = latData)

if __name__ == '__main__':
   app.run()