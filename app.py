
from flask import Flask, render_template, request, jsonify

from main import *

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("login.html")


@app.route('/bezoeker')
def Bezoeker():
    return render_template("bezoeker.html")


@app.route('/bezoeker/inschrijvingen')
def BezoekerInschrijvingen():
    return render_template("bezoeker/inschrijvingen.html", bezoeker=bezoeker1, presentaties=presentaties)


@app.route('/bezoeker/presentaties')
def BezoekerPresentaties():
    return render_template("bezoeker/presentaties.html", bezoeker=bezoeker1, presentaties=presentaties)


@app.route('/bezoeker/agenda')
def BezoekerAgenda():
    return render_template("bezoeker/agenda.html")


@app.route('/organisator')
def Organisator():
    return 'Organisator pagina'


# Api calls


# @app.route('/bezoeker_toevoegen_aan_presentatie_functie', methods=['POST'])
# def bezoeker_toevoegen_aan_presentatie_functie():
@app.route('/bezoeker_toevoegen_aan_presentatie_link', methods=['POST'])
def bezoeker_toevoegen_aan_presentatie_link():
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


@app.route('/bezoeker_verwijderen_van_presentatie_link', methods=['POST'])
def bezoeker_verwijderen_van_presentatie_link():
    data = request.json
    presentatie_id = data.get('presentatieId')
    bezoeker_id = data.get('bezoekerId')

    bezoeker_verwijderen_van_presentatie(
        bezoeker_id=bezoeker_id, presentatie_id=presentatie_id)

    return jsonify({
        "status": "success",
        "presentatieId": presentatie_id,
        "bezoekerId": bezoeker_id
    })
