import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None

        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None

        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None

        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Esame 10-09-2021", color="blue", size=24)
        self._page.controls.append(self._title)

        self._ddCitta = ft.Dropdown(label="Città (c)")
        self._controller.fillDDCities()
        self.btn_graph = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handle_graph)
        row1 = ft.Row([self._ddCitta, self.btn_graph],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._ddLocale1 = ft.Dropdown(label="Locale (b1)", width=400)
        self._btnLocaleDistante = ft.ElevatedButton(text="Locale distante",
                                                    on_click=self._controller.handle_locale_distante)
        row2 = ft.Row([self._ddLocale1, self._btnLocaleDistante], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._ddLocale2 = ft.Dropdown(label="Locale (b2)", width=400)
        self._btnPercorso = ft.ElevatedButton(text="Calcola percorso",
                                              on_click=self._controller.handle_percorso)
        row3 = ft.Row([self._ddLocale2, self._btnPercorso], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self._soglia = ft.TextField(label="Soglia (x)")
        row4 = ft.Row([self._soglia], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
