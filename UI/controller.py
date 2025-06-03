import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDStore(self):
        stores = self._model.getIdStores()

        for s in stores:
            self._view._ddStore.options.append(ft.dropdown.Option(text=s.store_id,
                                                                  data=s))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        pass
    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
