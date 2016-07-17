from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)
DB = DBHelper()
categories = ['treason', 'theft', 'oppression']

@app.route("/")
def home():
    crimes = DB.get_all_crimes()
    crimes = json.dumps(crimes)
    return render_template("home.html", crimes=crimes, categories=categories)

# def home():
#     try:
#         data = DB.get_all_inputs()
#     except Exception as e:
#         print e
#         data = None
#     return render_template("home.html", data=data)

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        print e
    return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    if category not in categories:
        return home()
    date = request.form.get("date")
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    description = request.form.get("description")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)

# AJDE BRAT!!!!!!!
