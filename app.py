
from flask import Flask, render_template, request

import requests



app = Flask(__name__)



VIN_DECODER_API = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json"



def decode_vin(vin):

    try:

        response = requests.get(VIN_DECODER_API.format(vin=vin))

        data = response.json()

        results = data.get("Results", [])



        def get_value(name):

            return next((item["Value"] for item in results if item["Variable"] == name), "")



        return {

            "year": get_value("Model Year"),

            "make": get_value("Make"),

            "model": get_value("Model"),

            "engine": get_value("Displacement (L)"),

            "drivetrain": get_value("Drive Type")

        }

    except Exception as e:

        print(f"VIN decoding error: {e}")

        return {}



@app.route("/", methods=["GET", "POST"])

def process():

    decoded = {}

    if request.method == "POST":

        vin = request.form.get("vin", "")

        decoded = decode_vin(vin)

    return render_template("processing.html", decoded=decoded)



@app.route("/review")

def review():
