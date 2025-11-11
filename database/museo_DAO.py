from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_all(self):

        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            return[]
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM museo"
        cursor.execute(query)

        musei=[]
        for row in cursor.fetchall():
            m = Museo(  id = row['id'],
                        nome = row['nome'],
                        tipologia = row['tipologia']
                        )
            musei.append(m)
        cursor.close()
        cnx.close()

        return musei



