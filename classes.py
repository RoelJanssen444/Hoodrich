
class Bezoeker(object):
    def __init__(self, bezoeker_id, naam, email, presentaties=[]):
        self.id = bezoeker_id
        self.naam = naam
        self.email = email
        self.presentaties = presentaties


class Presentator(object):
    def __init__(self, presentator_id, naam, presentaties=[]):
        self.id = presentator_id
        self.naam = naam
        self.presentaties = presentaties


class Presentatie(object):
    def __init__(self, presentatie_id, presentatie_naam, presentatie_beschrijving, lokaal_id, begin_tijd, eind_tijd, bezoekers=[], presentators=[]):
        self.id = presentatie_id
        self.naam = presentatie_naam
        self.beschrijving = presentatie_beschrijving
        self.bezoekers = bezoekers
        self.presentators = presentators
        self.lokaal_id = lokaal_id
        self.begin_tijd = begin_tijd
        self.eind_tijd = eind_tijd


class Lokaal(object):
    def __init__(self, lokaal_id):
        self.id = lokaal_id
