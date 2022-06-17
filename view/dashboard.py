from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "dashboard.kv"))

class DashboardWindow(MDBoxLayout):
    pass

class DashboardApp(MDApp):
    def build(self):
        return DashboardWindow()

if __name__ == "__main__":
    DashboardApp().run()