import flet as ft
from flet.core.types import MainAxisAlignment

from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None
        self.listview_artefatti = ft.ListView(expand= True, spacing = 10, auto_scroll= True)
    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def on_museo_change(self, e):
        museo_selezionato = e.control.value #leggo val dropdwn
        self.controller.museo_selezionato = museo_selezionato
    def on_epoca_change(self, e):
        epoca_selezionata = e.control.value
        self.controller.epoca_selezionata = epoca_selezionata

    def popola_lista_artefatti(self, artefatti):
        self.listview_artefatti.controls.clear()
        if not artefatti:
            self.alert.show_alert("No artefatti presenti")
        for artefatto in artefatti:
            self.listview_artefatti.controls.append(ft.Text(artefatto))
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self.dropdown_musei = ft.DropdownM2( label="Musei", options=[ft.dropdown.Option("Nessun filtro")]+[
                                                                   ft.dropdown.Option(museo) for museo in self.controller.get_lista_n_musei()],
                                            max_menu_height=200, width=250, on_change= self.on_museo_change)
        self.dropdown_epoche = ft.DropdownM2(label="epoche", options=[ft.dropdown.Option("Nessun filtro")]+ [
                                                                        ft.dropdown.Option(epoca) for epoca in self.controller.get_lista_epoca()],
                                             max_menu_height=200, width=250, on_change= self.on_epoca_change)

        # Sezione 3: Artefatti
        self.artefatti_button = ft.ElevatedButton(text="Mostra Artefatti", width=150, on_click = self.controller.sorta_artefatti)
        # TODO



        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row( controls=[self.dropdown_musei, self.dropdown_epoche],
                          spacing=300, alignment= ft.MainAxisAlignment.CENTER),
            # TODO
            self.artefatti_button,
            # Sezione 3: Artefatti
            ft.Divider(),
            self.listview_artefatti
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
