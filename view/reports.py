from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar

from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder

import json
import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "reports.kv"))

class EditDrawerReportsWindow(MDScreen):
    drawers_url = 'http://127.0.0.1:8000/drawers/'

    def update_drawer(self):
        d_id = self.ids.id
        d_date = self.ids.date
        d_operator = self.ids.operator
        d_opening_time = self.ids.opening_time
        d_float_zwl = self.ids.float_zwl
        d_float_usd = self.ids.float_usd
        d_status = self.ids.status
        d_expected_zwl = self.ids.expected_zwl
        d_actual_zwl = self.ids.actual_zwl
        d_expected_usd = self.ids.expected_usd
        d_actual_usd = self.ids.actual_usd
        d_card_sales = self.ids.card_sales
        d_ecocash_sales = self.ids.ecocash_sales
        d_closing_time = self.ids.closing_time

        id = d_id.text
        date = d_date.text
        operator = d_operator.text
        opening_time = d_opening_time.text
        float_zwl = d_float_zwl.text
        float_usd = d_float_usd.text
        status = d_status.text
        expected_zwl = d_expected_zwl.text
        actual_zwl = d_actual_zwl.text
        expected_usd = d_expected_usd.text
        actual_usd = d_actual_usd.text
        card_sales = d_card_sales.text
        ecocash_sales = d_ecocash_sales.text
        closing_time = d_closing_time.text
    

        d_id.text = ''
        d_date.text = ''
        d_operator.text = ''
        d_opening_time.text = ''
        d_float_zwl.text = ''
        d_float_usd.text = ''
        d_status.text = ''
        d_expected_zwl.text = ''
        d_actual_zwl.text = ''
        d_expected_usd.text = ''
        d_actual_usd.text = ''
        d_card_sales.text = ''
        d_ecocash_sales.text = ''
        d_closing_time.text = ''

        url = self.drawers_url + f'{id}'
        updated_drawer = {'id': id, 'date': date, 'operator': operator, 'opening_time': opening_time, 'float_zwl': float_zwl,
            'float_usd': float_usd, 'status': status, 'expected_zwl': expected_zwl, 'actual_zwl': actual_zwl, 'expected_usd': expected_usd,
            'actual_usd': actual_usd, 'card_sales': card_sales, 'ecocash_sales': ecocash_sales, 'closing_time': closing_time}
        updated_drawer_json = json.dumps(updated_drawer)
        UrlRequest(url, req_body=updated_drawer_json, method='PUT', on_success=self.drawer_updated)

    def drawer_updated(self, req, result):
        id = result['id']
        self.parent.parent.switch_screen("Drawer Reports Screen", "right")
        Snackbar(text = f'Drawer {id} Updated').open()

    def delete_drawer_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete drawer?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_drawer),
            ],
        )
        self.dialog.open()

    def delete_drawer(self, *args):
        d_id = self.ids.id
        id = d_id.text
        d_id.text = ''

        url = self.drawers_url + f'{id}'
        UrlRequest(url, method='DELETE', on_success=self.drawer_deleted)
    
    def drawer_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Drawer Reports Screen", "right")
        Snackbar(text = f'Drawer Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class DrawerReportsWindow(MDScreen):
    pass

class EditInventoryReportsWindow(MDScreen):
    pass

class InventoryReportsWindow(MDScreen):
    pass

class EditSalesReportsWindow(MDScreen):
    sales_url = 'http://127.0.0.1:8000/sales/'

    def update_drawer(self):
        d_id = self.ids.id
        d_date = self.ids.date
        d_operator = self.ids.operator
        d_opening_time = self.ids.opening_time
        d_float_zwl = self.ids.float_zwl
        d_float_usd = self.ids.float_usd
        d_status = self.ids.status
        d_expected_zwl = self.ids.expected_zwl
        d_actual_zwl = self.ids.actual_zwl
        d_expected_usd = self.ids.expected_usd
        d_actual_usd = self.ids.actual_usd
        d_card_sales = self.ids.card_sales
        d_ecocash_sales = self.ids.ecocash_sales
        d_closing_time = self.ids.closing_time

        id = d_id.text
        date = d_date.text
        operator = d_operator.text
        opening_time = d_opening_time.text
        float_zwl = d_float_zwl.text
        float_usd = d_float_usd.text
        status = d_status.text
        expected_zwl = d_expected_zwl.text
        actual_zwl = d_actual_zwl.text
        expected_usd = d_expected_usd.text
        actual_usd = d_actual_usd.text
        card_sales = d_card_sales.text
        ecocash_sales = d_ecocash_sales.text
        closing_time = d_closing_time.text
    

        d_id.text = ''
        d_date.text = ''
        d_operator.text = ''
        d_opening_time.text = ''
        d_float_zwl.text = ''
        d_float_usd.text = ''
        d_status.text = ''
        d_expected_zwl.text = ''
        d_actual_zwl.text = ''
        d_expected_usd.text = ''
        d_actual_usd.text = ''
        d_card_sales.text = ''
        d_ecocash_sales.text = ''
        d_closing_time.text = ''

        url = self.drawers_url + f'{id}'
        updated_drawer = {'id': id, 'date': date, 'operator': operator, 'opening_time': opening_time, 'float_zwl': float_zwl,
            'float_usd': float_usd, 'status': status, 'expected_zwl': expected_zwl, 'actual_zwl': actual_zwl, 'expected_usd': expected_usd,
            'actual_usd': actual_usd, 'card_sales': card_sales, 'ecocash_sales': ecocash_sales, 'closing_time': closing_time}
        updated_drawer_json = json.dumps(updated_drawer)
        UrlRequest(url, req_body=updated_drawer_json, method='PUT', on_success=self.drawer_updated)

    def drawer_updated(self, req, result):
        id = result['id']
        self.parent.parent.switch_screen("Drawer Reports Screen", "right")
        Snackbar(text = f'Drawer {id} Updated').open()

class SalesReportsWindow(MDScreen):
    pass
        
        

class ReportsMainWindow(MDScreen):
    pass

class ReportsWindow(MDBoxLayout):
    sales_url = 'http://127.0.0.1:8000/sales/'
    drawers_url = 'http://127.0.0.1:8000/drawers/'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(1,21):
            self.ids.reports_screen_manager.get_screen("Sales Reports Screen").ids.sales_reports_list.add_widget(OneLineAvatarListItem(text=f'Sale {i}'))
        #UrlRequest(self.sales_url, on_success=self.get_sales)
        UrlRequest(self.drawers_url, on_success=self.get_drawers)

    def get_drawers(self, request, result):
        for i in result:
            id = i['id']
            self.ids.reports_screen_manager.get_screen("Drawer Reports Screen").ids.drawer_reports_list.add_widget(
                OneLineAvatarListItem(text=f'{id} -- Drawer {id}', font_style="H5", 
                on_release= lambda instance: self.edit_drawer(instance.text)))
            #font_style="H5", bold=True, on_release= lambda instance: print(instance)

    def edit_drawer(self, instance):
        id = instance[0]
        url = self.drawers_url + f'{id}'
        UrlRequest(url, on_success=self.edit_drawer_screen)

    def edit_drawer_screen(self, request, result):
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.id.text = str(result['id'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.date.text = result['date']
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.operator.text = result['operator']
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.opening_time.text = result['opening_time']
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.float_zwl.text = str(result['float_zwl'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.float_usd.text = str(result['float_usd'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.status.text = result['status']
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.expected_zwl.text = str(result['expected_zwl'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.actual_zwl.text = str(result['actual_zwl'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.expected_usd.text = str(result['expected_usd'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.actual_usd.text = str(result['actual_usd'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.card_sales.text = str(result['card_sales'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.ecocash_sales.text = str(result['ecocash_sales'])
        self.ids.reports_screen_manager.get_screen("Edit Drawer Reports Screen").ids.closing_time.text = result['closing_time']
        self.switch_screen("Edit Drawer Reports Screen", "left")

    def switch_screen(self, screen_name, transition):
        self.ids.reports_screen_manager.transition.direction = transition
        self.ids.reports_screen_manager.current = screen_name

class ReportsApp(MDApp):
    def build(self):
        return ReportsWindow()

if __name__ == "__main__":
    ReportsApp().run()