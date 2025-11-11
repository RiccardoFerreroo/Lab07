from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        artefatti = self._artefatto_dao.get_all()
        musei = self._museo_dao.get_all()

        #trovo l'id del museo selezionato
        id_museo_selezionato = None
        if museo != None:
            for m in musei:
                if m.nome == museo:
                    id_museo_selezionato = m.id
                    break
        lista_artefatti_filtrati = []

        for a in artefatti:
            if museo == 'Nessun filtro' and epoca =='Nessun filtro':
                lista_artefatti_filtrati.append(a)
            elif museo != 'Nessun filtro' and epoca != 'Nessun filtro':
                if a.id_museo == id_museo_selezionato and a.epoca == epoca:
                    lista_artefatti_filtrati.append(a)
            elif museo == 'Nessun filtro' and epoca != 'Nessun filtro':
                if a.epoca == epoca:
                    lista_artefatti_filtrati.append(a)
            elif museo != 'Nessun filtro' and epoca == 'Nessun filtro':
                if a.id_museo == id_museo_selezionato:
                    lista_artefatti_filtrati.append(a)
        return lista_artefatti_filtrati





    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        artefatti =self._artefatto_dao.get_all()
        lista_epoche = set()
        for oggetto in artefatti:
            epoca = oggetto.epoca
            lista_epoche.add(epoca)
        return lista_epoche

        # TODO

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        lista_nomi_musei = []
        musei =self._museo_dao.get_all()
        for oggetto in musei:
            lista_nomi_musei.append(oggetto.nome)
        return lista_nomi_musei



