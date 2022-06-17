from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "users.kv"))

class EditUsersWindow(MDScreen):
    pass

class AddUsersWindow(MDScreen):
    pass

class UsersHomeWindow(MDScreen):
    pass

class UsersWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(1,21):
            self.ids.users_screen_manager.get_screen("Users Home Screen").ids.users_list.add_widget(OneLineAvatarListItem(text=f'User {i}'))

        #self.ids.users_home_screen.add_widget(UsersHomeWindow())
        #self.ids.add_users_screen.add_widget(AddUsersWindow())
        #self.ids.edit_users_screen.add_widget(EditUsersWindow())

    def switch_screen(self, screen_name, transition):
        self.ids.users_screen_manager.transition.direction = transition
        self.ids.users_screen_manager.current = screen_name

class UsersApp(MDApp):
    def build(self):
        return UsersWindow()

if __name__ == "__main__":
    UsersApp().run()