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
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def handle_dropdownBiblio(self):
        biblioteche= self._model.get_biblioteche()
        self._view.dd_biblioteca.options = [ft.dropdown.Option(key=str(b.id), text=b.nome) for b in biblioteche]
        self._view.page.update()
    def handle_dropdownGenere(self):
        generi = self._model.get_generi()
        self._view.dd_genere.options = [ft.dropdown.Option(key=str(g), text=str(g)) for g in generi]
        self._view.page.update()


    # CALLBACKS DROPDOWN
    def select_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value
    def select_genere(self, e):
        self.genere_selezionata = e.control.value


    # AZIONE: MOSTRA LIBRI
    def handle_mostra(self):
        biblioteca = self._view.dd_biblioteca.value
        genere = self._view.dd_genere.value
        lista = self._model.get_libri_filtrati(biblioteca,genere)
        for elemento in lista:
            self._view.lista_ricerca.controls.append(ft.Text(str(elemento)))
        self._view.update()
