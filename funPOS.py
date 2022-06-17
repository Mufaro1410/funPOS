from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

#from kivy.lang import Builder

from view import login, dashboard, register, inventory, users, reports

#import os

#dirname = os.path.dirname(__file__)

#Builder.load_file(os.path.join(dirname, "view/dashboard.kv"))

class MainWindow(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.dashboard.add_widget(dashboard.DashboardWindow())
        self.ids.register.add_widget(register.RegisterWindow())
        self.ids.inventory.add_widget(inventory.InventoryManagement())
        self.ids.users.add_widget(users.UsersWindow())
        self.ids.reports.add_widget(reports.ReportsWindow())

class funPOSWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.login_screen.add_widget(login.LoginWindow())
        self.ids.main_screen.add_widget(MainWindow())

    def switch_screen(self, screen_name, transition):
        self.ids.funpos_screen_manager.transition.direction = transition
        self.ids.funpos_screen_manager.current = screen_name

class funPOSApp(MDApp):
    def build(self):
        return funPOSWindow()

if __name__ == "__main__":
    funPOSApp().run()