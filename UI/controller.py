import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDCities(self):
        cities = self._model._cities
        for c in cities:
            self._view._ddCitta.options.append(ft.dropdown.Option(data=c, text=c, on_click=self.selectCity))

        self._view.update_page()

    def selectCity(self, e):
        if e.control.data is None:
            self._choiceCity = None
        else:
            self._choiceCity = e.control.data

    def selectBusiness1(self, e):
        if e.control.data is None:
            self._choiceBusiness1 = None
        else:
            self._choiceBusiness1 = e.control.data

    def selectBusiness2(self, e):
        if e.control.data is None:
            self._choiceBusiness2 = None
        else:
            self._choiceBusiness2 = e.control.data

    def handle_graph(self, e):
        self._model.crea_grafo(self._choiceCity)
        locali = self._model._nodes
        for l in locali:
            self._view._ddLocale1.options.append(ft.dropdown.Option(data=l, text=l.business_name, on_click=self.selectBusiness1))
            self._view._ddLocale2.options.append(ft.dropdown.Option(data=l, text=l.business_name, on_click=self.selectBusiness2))

        nNodi, nArchi = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."
                                                      f"Il grafo ha {nNodi} nodi e {nArchi} archi."))
        self._view.update_page()

    def handle_locale_distante(self, e):
        locale_distante, distanza = self._model.locale_distante(self._choiceBusiness1)
        self._view.txt_result.controls.append(ft.Text(f"Locale più distante: {locale_distante} --> {distanza}"))
        self._view.update_page()


    def handle_percorso(self, e):
        soglia = self._view._soglia.value
        try:
            floatSoglia = float(soglia)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Inserire una soglia numerica"))
            return
        distanza, cammino = self._model.getCammino(self._choiceBusiness1, self._choiceBusiness2, floatSoglia)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Distanza totale percorso: {distanza}"))
        for c in cammino:
            self._view.txt_result.controls.append(ft.Text(f"{c[1]} - {c[2]}"))
        self._view.update_page()