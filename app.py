from flask import Flask, render_template, request
import pandas as pd
import csv

app = Flask(__name__,template_folder= 'template')

@app.route('/')
def index():
    with open('pod-data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return render_template('task.html', data=data)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

    # Load the data here
    with open('pod-data.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Search the data
    #results = [row for row in data if query.lower() in row['Job Type'].lower()]
    results = [row for row in data if query.lower() in (row['Job Type'].lower() or row['Customer'].lower())]


    return render_template('task.html', data=results)

if __name__ == '__main__':
    app.run(debug=True)



