
from flask import Flask, render_template, request, jsonify

from main import *

app = Flask(__name__)

bezoekerId = 101


@app.route("/")
def Home():
    return render_template("login.html")


@app.route('/bezoeker')
def Bezoeker():
    return render_template("bezoeker.html", bezoekers=bezoekers,  presentaties=presentaties)


@app.route('/bezoeker/inschrijvingen')
def BezoekerInschrijvingen():
    return render_template("bezoeker/inschrijvingen.html", bezoekerId=bezoekerId, bezoekers=bezoekers)


@app.route('/bezoeker/presentaties')
def BezoekerPresentaties():
    return render_template("bezoeker/presentaties.html", bezoekers=bezoekers, presentaties=presentaties)


@app.route('/bezoeker/agenda')
def BezoekerAgenda():
    return render_template("bezoeker/agenda.html")


@app.route('/organisator')
def Organisator():
    return 'Organisator pagina'


# Api calls


# @app.route('/bezoeker_toevoegen_aan_presentatie_functie', methods=['POST'])
# def bezoeker_toevoegen_aan_presentatie_functie():
@app.route('/call_python_function', methods=['POST'])
def call_python_function():
    data = request.json
    presentatie_id = data.get('presentatieId')
    bezoeker_id = data.get('bezoekerId')

    bezoeker_toevoegen_aan_presentatie(
        bezoeker_id=bezoeker_id, presentatie_id=presentatie_id)

    return jsonify({
        "status": "success",
        "presentatieId": presentatie_id,
        "bezoekerId": bezoeker_id
    })
