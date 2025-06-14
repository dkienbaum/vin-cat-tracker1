from flask import Flask, render_template, request, redirect
import requests
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

def load_data():
   try:
       with open(DATA_FILE, "r") as f:
           return json.load(f)
   except:
       return []

def save_data(data):
   with open(DATA_FILE, "w") as f:
       json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
   vin_data = {}
   if request.method == "POST":
       vin = request.form.get("vin")
       aluminum = request.form.get("aluminum") == "on"
       steel = request.form.get("steel") == "on"
       refrigerant = request.form.get("refrigerant")
       converter_qty = request.form.get("converter_qty")
       date = datetime.now().strftime("%Y-%m-%d (%A)")

       # VIN decode
       try:
           response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/{vin}?format=json")
           result = response.json()["Results"][0]
           vin_data = {
               "vin": vin,
               "make": result.get("Make", ""),
               "model": result.get("Model", ""),
               "year": result.get("ModelYear", ""),
               "engine": result.get("EngineModel", ""),
               "drivetrain": result.get("DriveType", "")
           }
       except:
           vin_data = {
               "vin": vin,
               "make": "", "model": "", "year": "",
               "engine": "", "drivetrain": ""
           }

       entry = {
           "date": date,
           "vin": vin_data["vin"],
           "make": vin_data["make"],
           "model": vin_data["model"],
           "year": vin_data["year"],
           "engine": vin_data["engine"],
           "drivetrain": vin_data["drivetrain"],
           "aluminum_rims": aluminum,
           "steel_rims": steel,
           "refrigerant": refrigerant,
           "converter_qty": converter_qty
       }

       data = load_data()
       data.append(entry)
       save_data(data)

       return redirect("/review")

   return render_template("index.html")

@app.route("/review")
def review():
   data = load_data()
   return render_template("review.html", data=data)

if __name__ == "__main__":
   app.run(debug=True)
