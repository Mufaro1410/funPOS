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

Builder.load_file(os.path.join(dirname, "inventory.kv"))

class EditSuppliersWindow(MDScreen):
    suppliers_url = 'http://127.0.0.1:8000/suppliers/'

    def update_supplier(self):
        s_id = self.ids.id
        s_name = self.ids.supplier_name
        s_contact = self.ids.contact
        s_address = self.ids.address
        s_email = self.ids.email

        id = s_id.text
        supplier_name = s_name.text
        contact = s_contact.text
        address = s_address.text
        email = s_email.text

        s_id.text = ''
        s_name.text = ''
        s_contact.text = ''
        s_address.text = ''
        s_email.text = ''

        url =  f'{self.suppliers_url}{id}'
        updated_supplier = {"supplier_name": supplier_name, "contact": contact, "address": address, 
            "email": email}
        updated_supplier_json = json.dumps(updated_supplier)
        UrlRequest(url, req_body=updated_supplier_json, method='PUT', on_success=self.supplier_updated)


    def supplier_updated(self, req, result):
        supplier_name = result['supplier_name']
        self.parent.parent.switch_screen("Suppliers Home Screen", "right")
        Snackbar(text = f'{supplier_name} Updated').open()

    def delete_supplier_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete supplier?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_supplier),
            ],
        )
        self.dialog.open()

    def delete_supplier(self, *args):
        s_id = self.ids.id
        id = s_id.text
        #p_id.text = ''

        url = self.suppliers_url + f'{id}'
        UrlRequest(url, method='DELETE', on_success=self.supplier_deleted)
    
    def supplier_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Suppliers Home Screen", "right")
        Snackbar(text = f'Supplier Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddSuppliersWindow(MDScreen):
    suppliers_url = 'http://127.0.0.1:8000/suppliers/'

    def create_supplier(self):
        s_name = self.ids.supplier_name
        s_contact = self.ids.contact
        s_address = self.ids.address
        s_email = self.ids.email

        supplier_name = s_name.text
        contact = s_contact.text
        address = s_address.text
        email = s_email.text

        s_name.text = ''
        s_contact.text = ''
        s_address.text = ''
        s_email.text = ''

        new_supplier = {"supplier_name": supplier_name, "contact": contact, "address": address, 
            "email": email}
        new_supplier_json = json.dumps(new_supplier)
        UrlRequest(self.suppliers_url, req_body=new_supplier_json, method='POST', on_success=self.supplier_created)

    def supplier_created(self, req, result):
        supplier_name = result['supplier_name']
        self.parent.parent.switch_screen("Suppliers Home Screen", "right")
        Snackbar(text = f'{supplier_name} Created').open()

class SuppliersHomeWindow(MDScreen):
    suppliers_url = 'http://127.0.0.1:8000/suppliers/'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = []
        UrlRequest(self.suppliers_url, on_success=self.get_suppliers)

    def get_suppliers(self, request, result):
        for i in result:
            suppliers_dict = {}
            suppliers_dict['id'] = str(i['id'])
            suppliers_dict['supplier_name'] = i['supplier_name']
            self.data.append(suppliers_dict)
        self.set_search_suppliers()

    def set_search_suppliers(self, text="", search=False):
        '''Builds a list of users for the screen.'''

        def add_supplier_item(name):
            self.ids.suppliers_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_supplier(x),
                }
            )
        self.ids.suppliers_list.data = []
        for item in self.data:
            id = item['id']
            supplier_name = item['supplier_name']
            name = f'{id} - {supplier_name}'
            if search:
                if text in name:
                    add_supplier_item(name)
            else:
                add_supplier_item(name)

    def edit_supplier(self, name):
        id = name[0]
        suppliers_url = self.suppliers_url + f'{id}'
        UrlRequest(suppliers_url, on_success=self.edit_supplier_screen)
        
    def edit_supplier_screen(self, request, result):
        self.parent.get_screen("Edit Suppliers Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Suppliers Screen").ids.supplier_name.text = result['supplier_name']
        self.parent.get_screen("Edit Suppliers Screen").ids.contact.text = result['contact']
        self.parent.get_screen("Edit Suppliers Screen").ids.address.text = result['address']
        self.parent.get_screen("Edit Suppliers Screen").ids.email.text = result['email']
        self.parent.parent.switch_screen("Edit Suppliers Screen", "left")

class EditReceivingWindow(MDScreen):
    pass

class AddReceivingWindow(MDScreen):
    pass

class ReceivingHomeWindow(MDScreen):
    pass

class EditProductsWindow(MDScreen):
    products_url = 'http://127.0.0.1:8000/products/'

    def update_product(self):
        p_id = self.ids.id
        p_name = self.ids.product_name
        p_quantity = self.ids.quantity
        p_weight = self.ids.weight
        p_zwl = self.ids.price_zwl
        p_usd = self.ids.price_usd
        measurement_cat = self.ids.measurement_category

        id = p_id.text
        product_name = p_name.text
        quantity = p_quantity.text
        weight = p_weight.text
        price_zwl = p_zwl.text
        price_usd = p_usd.text
        measurement_category = measurement_cat.text

        p_id.text = ''
        p_name.text = ''
        p_quantity.text = '0'
        p_weight.text = '0.00'
        p_zwl.text = '0.00'
        p_usd.text = '0.00'
        measurement_cat.text = ''

        url = self.products_url + f'{id}'
        updated_product = {"product_name": product_name, "quantity": quantity, "weight": weight, 
            "price_zwl": price_zwl, "price_usd": price_usd, "measurement_category": measurement_category}
        updated_product_json = json.dumps(updated_product)
        UrlRequest(url, req_body=updated_product_json, method='PUT', on_success=self.product_updated)

    def product_updated(self, req, result):
        product_name = result['product_name']
        self.parent.parent.switch_screen("Products Home Screen", "right")
        Snackbar(text = f'{product_name} Updated').open()

    def delete_product_dialog(self):
        self.dialog = MDDialog(
            text="Are you sure you want to delete product?",
            buttons=[
                MDFlatButton(text="NO", on_release=self.close_dialog), 
                MDRaisedButton(text="YES", on_release=self.delete_product),
            ],
        )
        self.dialog.open()

    def delete_product(self, *args):
        p_id = self.ids.id
        id = p_id.text
        #p_id.text = ''

        url = self.products_url + f'{id}'
        UrlRequest(url, method='DELETE', on_success=self.product_deleted)
    
    def product_deleted(self, request, result):
        self.close_dialog()
        self.parent.parent.switch_screen("Products Home Screen", "right")
        Snackbar(text = f'Product Deleted').open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

class AddProductsWindow(MDScreen):
    products_url = 'http://127.0.0.1:8000/products/'

    def create_product(self):
        p_name = self.ids.product_name
        p_quantity = self.ids.quantity
        p_weight = self.ids.weight
        p_zwl = self.ids.price_zwl
        p_usd = self.ids.price_usd
        measurement_cat = self.ids.measurement_category

        product_name = p_name.text
        quantity = p_quantity.text
        weight = p_weight.text
        price_zwl = p_zwl.text
        price_usd = p_usd.text
        measurement_category = measurement_cat.text

        p_name.text = ''
        p_quantity.text = '0'
        p_weight.text = '0.00'
        p_zwl.text = '0.00'
        p_usd.text = '0.00'
        measurement_cat.text = ''

        new_product = {"product_name": product_name, "quantity": quantity, "weight": weight, 
            "price_zwl": price_zwl, "price_usd": price_usd, "measurement_category": measurement_category}
        new_product_json = json.dumps(new_product)
        UrlRequest(self.products_url, req_body=new_product_json, method='POST', on_success=self.product_created)

    def product_created(self, req, result):
        product_name = result['product_name']
        self.parent.parent.switch_screen("Products Home Screen", "right")
        Snackbar(text = f'{product_name} Created').open()

class ProductsHomeWindow(MDScreen):
    products_url = 'http://127.0.0.1:8000/products/'

    def __init__(self, **kw):
        super().__init__(**kw)
        self.data = []
        UrlRequest(self.products_url, on_success=self.get_products)

    def get_products(self, request, result):
        for i in result:
            products_dict = {}
            products_dict['id'] = str(i['id'])
            products_dict['product_name'] = i['product_name']
            self.data.append(products_dict)
        self.set_search_products()

    def set_search_products(self, text="", search=False):
        '''Builds a list of users for the screen.'''

        def add_product_item(name):
            self.ids.products_list.data.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": name,
                    "on_release": lambda x=name: self.edit_products(x),
                }
            )
        self.ids.products_list.data = []
        for item in self.data:
            id = item['id']
            product_name = item['product_name']
            name = f'{id} - {product_name}'
            if search:
                if text in name:
                    add_product_item(name)
            else:
                add_product_item(name)

    def edit_products(self, name):
        id = name[0]
        products_url = self.products_url + f'{id}'
        UrlRequest(products_url, on_success=self.edit_products_screen)
        
    def edit_products_screen(self, request, result):
        self.parent.get_screen("Edit Products Screen").ids.id.text = str(result['id'])
        self.parent.get_screen("Edit Products Screen").ids.product_name.text = result['product_name']
        self.parent.get_screen("Edit Products Screen").ids.quantity.text = str(result['quantity'])
        self.parent.get_screen("Edit Products Screen").ids.weight.text = str(result['weight'])
        self.parent.get_screen("Edit Products Screen").ids.price_zwl.text = str(result['price_zwl'])
        self.parent.get_screen("Edit Products Screen").ids.price_usd.text = str(result['price_usd'])
        self.parent.get_screen("Edit Products Screen").ids.measurement_category.text = result['measurement_category']
        self.parent.parent.switch_screen("Edit Products Screen", "left")

class InventoryManagementWindow(MDScreen):
    pass

class InventoryManagement(MDBoxLayout):
    def switch_screen(self, screen_name, transition):
        self.ids.inventory_screen_manager.transition.direction = transition
        self.ids.inventory_screen_manager.current = screen_name

class InventoryApp(MDApp):
    def build(self):
        return InventoryManagement()

if __name__ == "__main__":
    InventoryApp().run()
