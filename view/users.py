from logging import root
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineAvatarListItem, OneLineListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.uix.screenmanager import ScreenManager
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder

import os
import json

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "users.kv"))

class EditCustomersWindow(MDScreen):
    customers_url = 'http://127.0.0.1:8000/customers/'

    def update_customer(self):
        c_id = self.ids.id
        c_title = self.ids.title
        l_name = self.ids.last_name
        f_name = self.ids.first_name
        c_contact = self.ids.contact
        mail = self.ids.email
        addrss = self.ids.address

        id = c_id.text
        title = c_title.text
        last_name = l_name.text
        first_name = f_name.text
        contact = c_contact.text
        email = mail.text
        address = addrss.text

        c_id.text = ''
        c_title.text = ''
        f_name.text = ''
        l_name.text = ''
        c_contact.text = ''
        mail.text = ''
        addrss.text = ''

        url = self.customers_url + f'{id}'
        updated_customer = {"title": title, "last_name": last_name, "first_name": first_name, "contact": contact, "email": email, "address": address}
        updated_customer_json = json.dumps(updated_customer)
        UrlRequest(url, req_body=updated_customer_json, method='PUT', on_success=self.customer_updated)

    def customer_updated(self, req, result):
        title = result['title']
        first_name = result['first_name']
        last_name = result['last_name']
        self.parent.parent.switch_screen("Customers Home Screen", "right")
        Snackbar(text = f'{title} {first_name} {last_name} Updated').open()

    def delete_customer_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete customer?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_customer),
            ],
        )
        self.dialog.open()

    def delete_customer(self, *args):
        id_ = self.ids.id
        id = id_.text
        id_.text = ''

        url = self.customers_url + f'{id}'
        UrlRequest(url, method='DELETE', on_success=self.customer_deleted)
    
    def customer_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Customers Home Screen", "right")
        Snackbar(text = f'Customer Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddCustomersWindow(MDScreen):
    customers_url = 'http://127.0.0.1:8000/customers/'

    def create_customer(self):
        c_title = self.ids.title
        l_name = self.ids.last_name
        f_name = self.ids.first_name
        c_contact = self.ids.contact
        mail = self.ids.email
        addrss = self.ids.address

        title = c_title.text
        last_name = l_name.text
        first_name = f_name.text
        contact = c_contact.text
        email = mail.text
        address = addrss.text

        c_title.text = ''
        l_name.text = ''
        f_name.text = ''
        c_contact.text = ''
        mail.text = ''
        addrss.text = ''

        new_customer = {"title": title, "last_name": last_name, "first_name": first_name, "contact": contact, "email": email, "address": address}
        new_customer_json = json.dumps(new_customer)
        UrlRequest(self.customers_url, req_body=new_customer_json, on_success=self.customer_created)

    def customer_created(self, req, result):
        title = result['title']
        first_name = result['first_name']
        last_name = result['last_name']
        self.parent.parent.switch_screen("Customers Home Screen", "right")
        Snackbar(text = f'{title} {last_name} {first_name} Created').open()

class CustomersHomeWindow(MDScreen):
    customers_url = 'http://127.0.0.1:8000/customers/'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = []
        UrlRequest(self.customers_url, on_success=self.get_customers)

    def get_customers(self, request, result):
        for i in result:
            customer_dict = {}
            customer_dict['id'] = str(i['id'])
            customer_dict['title'] = i['title']
            customer_dict['last_name'] = i['last_name']
            customer_dict['first_name'] = i['first_name']
            self.data.append(customer_dict)
        self.set_search_customers()

    def set_search_customers(self, text="", search=False):
        '''Builds a list of users for the screen.'''

        def add_customer_item(name):
            self.ids.customers_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_customer(x),
                }
            )
        self.ids.customers_list.data = []
        for item in self.data:
            id = item['id']
            title = item['title']
            first_name = item['first_name']
            last_name = item['last_name']
            name = f'{id} - {title} {first_name} {last_name}'
            if search:
                if text in name:
                    add_customer_item(name)
            else:
                add_customer_item(name)

    def edit_customer(self, name):
        id = name[0]
        url = self.customers_url + f'{id}'
        UrlRequest(url, on_success=self.edit_customer_screen)

    def edit_customer_screen(self, request, result):
        self.parent.get_screen("Edit Customers Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Customers Screen").ids.title.text = result['title']
        self.parent.get_screen("Edit Customers Screen").ids.first_name.text = result['first_name']
        self.parent.get_screen("Edit Customers Screen").ids.last_name.text = result['last_name']
        self.parent.get_screen("Edit Customers Screen").ids.contact.text = result['contact']
        self.parent.get_screen("Edit Customers Screen").ids.email.text = result['email']
        self.parent.get_screen("Edit Customers Screen").ids.address.text = result['address']
        self.parent.parent.switch_screen("Edit Customers Screen", "left")

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

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

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
    
    """
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''
        Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        # get the tab icon.
        count_icon = instance_tab.icon
        # print it on shell/bash.
        print(f"Welcome to {count_icon}' tab'")
    """

#class CustomOneLineListItem(OneLineListItem):
#    pass

class UsersHomeWindow(MDScreen):
    users_url = 'http://127.0.0.1:8000/users/'
    credentials_url = 'http://127.0.0.1:8000/credentials/'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = []
        UrlRequest(self.users_url, on_success=self.get_users)

    def get_users(self, request, result):
        for i in result:
            user_dict = {}
            user_dict['id'] = str(i['id'])
            user_dict['first_name'] = i['first_name']
            user_dict['last_name'] = i['last_name']
            self.data.append(user_dict)
        self.set_search_users()

    def set_search_users(self, text="", search=False):
        '''Builds a list of users for the screen.'''

        def add_user_item(name):
            self.ids.users_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_user(x),
                }
            )
        self.ids.users_list.data = []
        for item in self.data:
            id = item['id']
            first_name = item['first_name']
            last_name = item['last_name']
            name = f'{id} - {first_name} {last_name}'
            if search:
                if text in name:
                    add_user_item(name)
            else:
                add_user_item(name)

    def edit_user(self, name):
        id = name[0]
        users_url = self.users_url + f'{id}'
        credentials_url = self.credentials_url + f'{id}'
        UrlRequest(users_url, on_success=self.edit_user_screen)
        UrlRequest(credentials_url, on_success=self.edit_user_credentials_screen)

    def edit_user_screen(self, request, result):
        self.parent.get_screen("Edit Users Screen").ids.u_id.text = str(result['id'])
        self.parent.get_screen("Edit Users Screen").ids.first_name.text = result['first_name']
        self.parent.get_screen("Edit Users Screen").ids.last_name.text = result['last_name']
        self.parent.get_screen("Edit Users Screen").ids.date_of_birth.text = result['date_of_birth']
        self.parent.get_screen("Edit Users Screen").ids.gender.text = result['gender']
        self.parent.get_screen("Edit Users Screen").ids.email.text = result['cell']
        self.parent.get_screen("Edit Users Screen").ids.cell.text = result['email']
        self.parent.get_screen("Edit Users Screen").ids.address.text = result['address']

    def edit_user_credentials_screen(self, request, result):
        # filling user credentials
        self.parent.get_screen("Edit Users Screen").ids.c_id.text = str(result['id'])
        self.parent.get_screen("Edit Users Screen").ids.username.text = result['username']
        self.parent.get_screen("Edit Users Screen").ids.password.text = result['password']
        self.parent.get_screen("Edit Users Screen").ids.designation.text = result['designation']
        self.parent.get_screen("Edit Users Screen").ids.user_id.text = str(result['user_id'])
        # filling reset credentials
        self.parent.get_screen("Edit Users Screen").ids.r_id.text = str(result['id'])
        self.parent.get_screen("Edit Users Screen").ids.r_username.text = result['username']
        self.parent.get_screen("Edit Users Screen").ids.new_password.text = ''
        self.parent.get_screen("Edit Users Screen").ids.re_new_password.text = ''
        self.parent.parent.switch_screen("Edit Users Screen", "left")

class UsersManagementWindow(MDScreen):
    pass

class UsersWindow(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.users_screen_manager.transition.direction = transition
        self.ids.users_screen_manager.current = screen_name

class UsersApp(MDApp):
    def build(self):
        return UsersWindow()

if __name__ == "__main__":
    UsersApp().run()