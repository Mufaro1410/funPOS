from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.uix.screenmanager import ScreenManager
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import os
import json

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "users.kv"))

class EditUsersWindow(MDScreen):
    users_url = 'http://127.0.0.1:8000/users/'
    user_credentials_url = 'http://127.0.0.1:8000/credentials/'

    def update_user(self):
        id_ = self.ids.u_id
        f_name = self.ids.first_name
        l_name = self.ids.last_name
        dob = self.ids.date_of_birth
        gndr = self.ids.gender
        mail = self.ids.email
        cel = self.ids.cell
        addrss = self.ids.address

        id = id_.text
        first_name = f_name.text
        last_name = l_name.text
        date_of_birth = dob.text
        gender = gndr.text
        email = mail.text
        cell = cel.text
        address = addrss.text

        id_.text = ''
        f_name.text = ''
        l_name.text = ''
        dob.text = ''
        gndr.text = ''
        mail.text = ''
        cel.text = ''
        addrss.text = ''

        url = self.users_url + f'{id}'
        updated_user = {"first_name": first_name, "last_name": last_name, "date_of_birth": date_of_birth, 
            "gender": gender, "email": email, "cell": cell, "address": address}
        updated_user_json = json.dumps(updated_user)
        UrlRequest(url, req_body=updated_user_json, method='PUT', on_success=self.user_updated)

    def user_updated(self, req, result):
        first_name = result['first_name']
        last_name = result['last_name']
        #self.parent.parent.switch_screen("Users Home Screen", "right")
        Snackbar(text = f'User {first_name} {last_name} Updated').open()

    def delete_user_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete user?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_user),
            ],
        )
        self.dialog.open()

    def delete_user(self, *args):
        id_ = self.ids.u_id
        id = id_.text
        id_.text = ''

        url = self.users_url + f'{id}'
        UrlRequest(url, method='DELETE', on_success=self.user_deleted)
    
    def user_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Users Home Screen", "right")
        Snackbar(text = f'User Deleted').open()

    def update_credential(self):
        c_id = self.ids.c_id
        u_name = self.ids.username
        pword = self.ids.password
        des = self.ids.designation
        u_id = self.ids.user_id

        id = c_id.text
        username = u_name.text
        password = pword.text
        designation = des.text
        user_id = u_id.text

        c_id.text = ''
        u_name.text = ''
        pword.text = ''
        des.text = ''
        u_id.text = ''

        url = self.user_credentials_url + f'{id}'
        updated_user_credential = {"username": username, "password": password, "designations": designation, 
            "user_id": user_id}
        updated_user_credential_json = json.dumps(updated_user_credential)
        UrlRequest(url, req_body=updated_user_credential_json, method='PUT', on_success=self.user_credential_updated)

    def user_credential_updated(self, req, result):
        first_name = result['first_name']
        last_name = result['last_name']
        #self.parent.parent.switch_screen("Users Home Screen", "right")
        Snackbar(text = f'User {first_name} {last_name} Updated').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddUsersWindow(MDScreen):
    users_url = 'http://127.0.0.1:8000/users/'
    credentials_url = 'http://127.0.0.1:8000/credentials/'

    def create_user(self):
        f_name = self.ids.first_name
        l_name = self.ids.last_name
        dob = self.ids.date_of_birth
        gndr = self.ids.gender
        mail = self.ids.email
        cel = self.ids.cell
        addrss = self.ids.address

        first_name = f_name.text
        last_name = l_name.text
        date_of_birth = dob.text
        gender = gndr.text
        email = mail.text
        cell = cel.text
        address = addrss.text

        f_name.text = ''
        l_name.text = ''
        dob.text = ''
        gndr.text = ''
        mail.text = ''
        cel.text = ''
        addrss.text = ''

        new_user = {"first_name": first_name, "last_name": last_name, "date_of_birth": date_of_birth, 
            "gender": gender, "email": email, "cell": cell, "address": address}
        new_user_json = json.dumps(new_user)
        UrlRequest(self.users_url, req_body=new_user_json, method='POST', on_success=self.user_created)

    def user_created(self, req, result):
        first_name = result['first_name']
        last_name = result['last_name']
        self.parent.parent.switch_screen("Users Home Screen", "right")
        Snackbar(text = f'User {first_name} {last_name} Created').open()

    def create_user_credential(self):
        uname = self.ids.username
        pword = self.ids.password
        des = self.ids.designation
        u_id = self.ids.user_id

        username = uname.text
        password = pword.text
        designation = des.text
        user_id = u_id.text

        uname.text = ''
        pword.text = ''
        des.text = ''
        u_id.text = ''

        new_user_credential = {"username": username, "password": password, "designation": designation, "user_id": user_id}
        new_user_credential_json = json.dumps(new_user_credential)
        UrlRequest(self.credentials_url, req_body=new_user_credential_json, method='POST', on_success=self.user_credential_created)

    def user_credential_created(self, req, result):
        username = result['username']
        self.parent.parent.switch_screen("Users Home Screen", "right")
        Snackbar(text = f'User Credential {username} Created').open()

class UsersHomeWindow(MDScreen):
    pass

class UsersWindow(MDBoxLayout):
    users_url = 'http://127.0.0.1:8000/users/'
    credentials_url = 'http://127.0.0.1:8000/credentials/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        UrlRequest(self.users_url, on_success=self.get_users)

    def get_users(self, request, result):
        for i in result:
            id = i['id']
            first_name = i['first_name']
            last_name = i['last_name']
            self.ids.users_screen_manager.get_screen("Users Home Screen").ids.users_list.add_widget(
                OneLineAvatarListItem(text=f'{id} -- {first_name} {last_name}', font_style="H5", 
                on_release= lambda instance: self.edit_user(instance.text)))
            #font_style="H5", bold=True, on_release= lambda instance: print(instance)

    def edit_user(self, instance):
        id = instance[0]
        users_url = self.users_url + f'{id}'
        credentials_url = self.credentials_url + f'{id}'
        UrlRequest(users_url, on_success=self.edit_user_screen)
        UrlRequest(credentials_url, on_success=self.edit_user_credentials_screen)

    def edit_user_screen(self, request, result):
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.u_id.text = str(result['id'])
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.first_name.text = result['first_name']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.last_name.text = result['last_name']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.date_of_birth.text = result['date_of_birth']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.gender.text = result['gender']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.email.text = result['cell']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.cell.text = result['email']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.address.text = result['address']

    def edit_user_credentials_screen(self, request, result):
        # filling user credentials
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.c_id.text = str(result['id'])
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.username.text = result['username']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.password.text = result['password']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.designation.text = result['designation']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.user_id.text = str(result['user_id'])
        # filling reset credentials
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.r_id.text = str(result['id'])
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.r_username.text = result['username']
        self.ids.users_screen_manager.get_screen("Edit Users Screen").ids.r_password.text = result['password']
        self.switch_screen("Edit Users Screen", "left")

    def switch_screen(self, screen_name, transition):
        self.ids.users_screen_manager.transition.direction = transition
        self.ids.users_screen_manager.current = screen_name

class UsersApp(MDApp):
    def build(self):
        return UsersWindow()

if __name__ == "__main__":
    UsersApp().run()