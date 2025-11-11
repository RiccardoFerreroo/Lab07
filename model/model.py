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
        if museo == None or epoca == None:
            return []
        lista_artefatti_filtrati = []
        artefatti = self._artefatto_dao.get_all()

        for oggetto in artefatti:
            if oggetto.id_museo == museo and oggetto.epoca == epoca:
                lista_artefatti_filtrati.append(oggetto)
                #Visualizzare gli artefatti in uno specifico museo di una specifica epoca
            elif museo == 'Nessun filtro' and epoca == 'Nessun filtro':
                lista_artefatti_filtrati.append(oggetto)
                # Visualizzare gli artefatti presenti in tutti i musei
            elif oggetto.id_museo == museo and epoca == 'Nessun filtro':
                lista_artefatti_filtrati.append(oggetto)
                # Visualizzare gli artefatti presenti in uno specifico museo
            elif museo == 'Nessun filtro' and oggetto.epoca == epoca:
                lista_artefatti_filtrati.append(oggetto)
                # Visualizzare gli artefatti di una specifica epoca
            else:
                pass

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



