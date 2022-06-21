from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem

from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "register.kv"))

class CloseDrawerWindow(MDScreen):
    pass

class FinalPaymentProcessingWindow(MDScreen):
    pass

class PaymentSplitWindow(MDScreen):
    pass

class PaymentProcessingWindow(MDScreen):
    pass

class RegisterMainWindow(MDScreen):
    pass

class DrawerIdDialog(MDBoxLayout):
    pass

class OpenDrawerWindow(MDScreen):
    drawers_url = 'http://127.0.0.1:8000/drawers/'

    def start_register_drawer(self):
        date = '2022-06-21'
        operator = 'mufaro'
        opening_time = '0800'
        float_zwl = self.ids.float_zwl.text
        float_usd = self.ids.float_usd.text
        status = 'Open'
        expected_zwl = 0.0
        actual_zwl = 0.0
        expected_usd = 0.0
        actual_usd = 0.0
        ecocash_sales = 0.0
        card_sales = 0.0
        closing_time = ''

        open_drawer_data = {'date': date, 'operator': operator, 'opening_time': opening_time, 'float_zwl': float_zwl,
            'float_usd': float_usd, 'status': status, 'expected_zwl': expected_zwl, 'actual_zwl': actual_zwl, 'expected_usd': expected_usd,
            'actual_usd': actual_usd, 'ecocash_sales': ecocash_sales, 'card_sales': card_sales, 'closing_time': closing_time}
        open_drawer_data_json = json.dumps(open_drawer_data)
        UrlRequest(self.drawers_url, req_body=open_drawer_data_json, on_success=self.display_new_drawer)

    def display_new_drawer(self, req, result):
        self.ids.start_drawer_button.disabled = True
        self.ids.confirm_start_drawer_button.disabled = False

        id = result['id']
        date = result['date']
        operator = result['operator']
        opening_time = result['opening_time']
        float_zwl = result['float_zwl']
        float_usd = result['float_usd']
        status = result['status']
        expected_zwl = result['expected_zwl']
        actual_zwl = result['actual_zwl']
        expected_usd = result['expected_usd']
        actual_usd = result['actual_usd']
        ecocash_sales = result['ecocash_sales']
        card_sales = result['card_sales']
        closing_time = result['closing_time']

        drawer_dict = {"id": id, 'date': date, 'operator': operator, 'starting_time': opening_time, 'float_zwl': float_zwl, 
            'float_usd': float_usd, 'status': status, 'expected_zwl': expected_zwl, 'actual_zwl': actual_zwl, 'expected_usd': expected_usd,
            'actual_usd': actual_usd, 'ecocash_sales': ecocash_sales, 'swipe_sales': card_sales, 'ending_time': closing_time}
        for key, value in drawer_dict.items():
            self.ids.display_new_drawer_items.add_widget(OneLineIconListItem(text=f'{key}: {value}'))

    def confirm_start_register_drawer(self):
        self.parent.parent.switch_screen('Register Main Screen', 'left')
        self.ids.display_new_drawer_items.clear_widgets()
        self.ids.float_zwl.text = '0.00'
        self.ids.float_usd.text = '0.00'
        self.ids.start_drawer_button.disabled = False
        self.ids.confirm_start_drawer_button.disabled = True
    
    def resume_register_dialog(self, *args):
        self.dialog = MDDialog(
            title = 'Enter Drawer ID',
            type = 'custom',
            content_cls = DrawerIdDialog(),
            buttons=[
                MDFlatButton(
                    text = "CANCEL",
                    on_release = self.close_dialog
                ),
                MDRaisedButton(
                    text="NEXT", md_bg_color=[1, 0, 1, 1],
                    on_release = self.resume_register_drawer
                ),
            ],
        )
        self.dialog.open()
        
    def resume_register_drawer(self, *args):
        id = self.dialog.content_cls.ids.drawer_id_dialog.text
        url = self.drawers_url + f'{id}'
        UrlRequest(url, on_success=self.verify_register)

    def verify_register(self, req, result):
        self.parent.parent.switch_screen('Register Main Screen', 'left')
        self.close_dialog()
        '''
        username = 'mufaro'
        if result['operator'] == username and result['status'] == 'Open':
            self.close_dialog()
            self.parent.parent.transition.direction = 'left'
            self.parent.parent.current = 'Register Screen'
        else:
            self.close_dialog()
            self.dialog = MDDialog(
                title='Resumption Failure',
                text="Can't resume drawer you're not the right user or drawer is closed",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        #text_color=self.theme_cls.primary_color,
                        on_release=self.close_dialog
                    ),
                ],
            )
            self.dialog.open()
        '''

    def close_dialog(self, *args):
        self.dialog.dismiss()

class RegisterWindow(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.register_screen_manager.transition.direction = transition
        self.ids.register_screen_manager.current = screen_name

class RegisterApp(MDApp):
    def build(self):
        return RegisterWindow()

if __name__ == "__main__":
    RegisterApp().run()