from flask import Flask, render_template, request

import requests



app = Flask(__name__)



VIN_DECODER_API = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{}?format=json"



@app.route('/', methods=['GET', 'POST'])

def index():

    decoded = {}

    if request.method == 'POST':

        vin = request.form['vin']

        response = requests.get(VIN_DECODER_API.format(vin))

        data = response.json()

        for item in data['Results']:

            if item['Variable'] == 'Make':

                decoded['make'] = item['Value']

            elif item['Variable'] == 'Model':

                decoded['model'] = item['Value']

            elif item['Variable'] == 'Model Year':

                decoded['year'] = item['Value']

            elif item['Variable'] == 'Engine Model':

                decoded['engine'] = item['Value']

            elif item['Variable'] == 'Drive Type':

                decoded['drivetrain'] = item['Value']

    return render_template('processing.html', decoded=decoded)
