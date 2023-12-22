
from classes import *
from flask import jsonify

bezoeker1 = Bezoeker(101, "sjef", "voorbeel@gmil.com", ["403", "404"])
bezoeker2 = Bezoeker(102, "emma", "emma@email.com")
bezoeker3 = Bezoeker(103, "thomas", "thomas@example.com")
bezoeker4 = Bezoeker(104, "lisa", "lisa@mail.com")
bezoeker5 = Bezoeker(105, "peter", "peter@example.org")
bezoeker6 = Bezoeker(106, "sara", "sara@gmail.com")
bezoekers = [
    bezoeker1,
    bezoeker2,
    bezoeker3,
    bezoeker4,
    bezoeker5,
    bezoeker6,
]

organisator1 = Presentator(201, "Fred")
organisator2 = Presentator(202, "Sophie")
organisator3 = Presentator(203, "Mike")
organisator4 = Presentator(204, "Anna")
organisators = [
    organisator1,
    organisator2,
    organisator3,
    organisator4,
]


lokaal1 = Lokaal(301)
lokaal2 = Lokaal(302)
lokaal3 = Lokaal(303)
lokaal4 = Lokaal(304)
lokaal5 = Lokaal(305)
lokaal6 = Lokaal(306)
lokaal7 = Lokaal(307)
lokaal8 = Lokaal(308)
lokalen = [
    lokaal1,
    lokaal2,
    lokaal3,
    lokaal4,
    lokaal5,
    lokaal6,
    lokaal7,
    lokaal8,
]

presentaties = [
    Presentatie(401, "Presentatie 1", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal1.id, "10:00", "11:30", [bezoeker1, bezoeker2], [organisator1, organisator2]),
    Presentatie(402, "Presentatie 2", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal2.id, "12:00", "13:30", [bezoeker3, bezoeker4], [organisator3, organisator4]),
    Presentatie(403, "Presentatie 3", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal3.id, "14:00", "15:30", [bezoeker5, bezoeker6], [organisator1, organisator2]),
    Presentatie(404, "Presentatie 4", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal4.id, "16:00", "17:30", [bezoeker1, bezoeker3], [organisator3, organisator4]),
    Presentatie(405, "Presentatie 5", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal5.id, "18:00", "19:30", [bezoeker2, bezoeker4], [organisator1, organisator2]),
    Presentatie(406, "Presentatie 6", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal6.id, "20:00", "21:30", [bezoeker5, bezoeker6], [organisator3, organisator4]),
    Presentatie(407, "Presentatie 7", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal7.id, "22:00", "23:30", [bezoeker1, bezoeker3, bezoeker5], [organisator1, organisator2]),
    Presentatie(408, "Presentatie 8", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley.",
                lokaal8.id, "09:00", "10:30", [bezoeker2, bezoeker4, bezoeker6], [organisator3, organisator4]),
]


def vind_presentatie(presentatie_id):
    huidig_id = int(presentatie_id)
    for presentatie in presentaties:
        if presentatie.id == huidig_id:
            return presentatie
    return None


def vind_bezoeker(bezoeker_id):
    huidig_id = int(bezoeker_id)
    for bezoeker in bezoekers:
        if bezoeker.id == huidig_id:
            return bezoeker
    return None


def bezoeker_toevoegen_aan_presentatie(bezoeker_id, presentatie_id):
    # Your Python logic here
    print("Python function executed!")

    # print(bezoeker_id)
    # print(presentatie_id)
    target_presentatie = (
        presentatie for presentatie in presentaties if presentatie.id == presentatie_id)
    # print(target_presentatie)

    huidige_presentatie = vind_presentatie(presentatie_id)
    # print(huidige_presentatie.bezoekers)
    huidige_presentatie.bezoekers.append("aosjdlnkm;")

    huidige_bezoeker = vind_bezoeker(bezoeker_id)
    huidige_bezoeker.presentaties.append(presentatie_id)

    print("huidige_bezoeker")
    print(huidige_bezoeker)
    # print(huidige_presentatie.bezoekers)
    # print("huidige_presentatie")
    # print(huidige_presentatie)
    # print(huidige_presentatie.naam)

    return jsonify({"status": "success"})


def bezoeker_verwijderen_van_presentatie(bezoeker_id, presentatie_id):
    print("Python function executed!")
    print("bezoeker verwijderen van presentatie")

    print(bezoeker_id)
    print(presentatie_id)
    huidige_bezoeker = vind_bezoeker(bezoeker_id)
    print("huidige_bezoeker")
    print(huidige_bezoeker)
    print(huidige_bezoeker.presentaties)
    huidige_bezoeker.presentaties.remove(presentatie_id)
    print(huidige_bezoeker.presentaties)

    # huidige_presentatie = vind_presentatie(presentatie_id)
    # # print(huidige_presentatie.bezoekers)
    # huidige_presentatie.bezoekers.append("aosjdlnkm;")

    # huidige_bezoeker = vind_bezoeker(bezoeker_id)
    # huidige_bezoeker.presentaties.append(presentatie_id)

    # print("huidige_bezoeker")
    # print(huidige_bezoeker)
    # print(huidige_presentatie.bezoekers)
    # print("huidige_presentatie")
    # print(huidige_presentatie)
    # print(huidige_presentatie.naam)

    return jsonify({"status": "success"})
