from database.DB_connect import ConnessioneDB
from database.museo_DAO import MuseoDAO
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_all(self):
        "leggo database per ottenere gli artefatti"
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            return[]
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM artefatto"
        cursor.execute(query)

        artefatti = []
        for row in cursor.fetchall():
            a = Artefatto(  id= row['id'],
                            nome =row['nome'],
                            tipologia= row['tipologia'],
                            epoca= row['epoca'],
                            id_museo = row['id_museo'])
            artefatti.append(a)
        cursor.close()
        cnx.close()
        return artefatti



