from flask import Flask, render_template, request



app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])

def index():

    decoded = {

        "year": "",

        "make": "",

        "model": "",

        "engine": "",

        "drivetrain": ""

    }



    if request.method == "POST":

        vin = request.form["vin"]



        # TEMP FAKE DATA: Replace this later with real VIN decoder

        if len(vin) >= 8:

            decoded["year"] = "2012"

            decoded["make"] = "Chevrolet"

            decoded["model"] = "Impala"

            decoded["engine"] = "3.6L V6"

            decoded["drivetrain"] = "FWD"



    return render_template("processing.html", decoded=decoded)