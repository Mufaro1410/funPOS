from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel

from kivy.properties import ObjectProperty
from kivy.lang import Builder
from matplotlib.pyplot import text

from view import login, dashboard, register, inventory, users, reports

# import os

# dirname = os.path.dirname(__file__)

# Builder.load_file(os.path.join(dirname, "view/funpos.kv"))

class NavItem(MDBottomNavigationItem):
    '''class that defines the Bottom Navigation Items'''
    pass

class MainWindow(MDScreen):
    '''class that defines the bottom navigation panel'''
    bottom_navigation = ObjectProperty()

class funPOSWindow(MDBoxLayout):
    '''the root widget class'''

    def __init__(self, **kwargs):
        super(funPOSWindow, self).__init__(**kwargs)

        self.ids.login_screen.add_widget(login.LoginWindow())

        bottom_nav = self.ids.main_screen.bottom_navigation

        dash = NavItem(name='Home Screen', text='home', icon='home')
        dash.add_widget(dashboard.DashboardWindow())
        bottom_nav.add_widget(dash)

        reg = NavItem(name='Register Screen', text='register', icon='cash-register')
        reg.add_widget(register.RegisterWindow())
        bottom_nav.add_widget(reg)

        inv = NavItem(name='Inventory Screen', text='inventory', icon='file-table')
        inv.add_widget(inventory.InventoryManagement())
        bottom_nav.add_widget(inv)

        usrs = NavItem(name='Users Screen', text='users', icon='account-tie')
        usrs.add_widget(users.UsersWindow())
        bottom_nav.add_widget(usrs)

        rep = NavItem(name='Reports Screen', text='reports', icon='chart-line')
        rep.add_widget(reports.ReportsWindow())
        bottom_nav.add_widget(rep)

class funPOSApp(MDApp):
    def build(self):
        return funPOSWindow()

if __name__ == "__main__":
    funPOSApp().run()