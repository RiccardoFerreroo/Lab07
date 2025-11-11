import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def get_lista_n_musei(self):
       return self._model.get_musei()

    def get_lista_epoca(self):
        return self._model.get_epoche()

    # CALLBACKS DROPDOWN
    # qua vado al model e faccio il sorting
    def sorta_artefatti(self,e ):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata
        artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        if artefatti:
            self._view.popola_lista_artefatti(artefatti)


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
