from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "inventory.kv"))

class EditSuppliersWindow(MDScreen):
    pass

class AddSuppliersWindow(MDScreen):
    pass

class SuppliersHomeWindow(MDScreen):
    pass

class EditReceivingWindow(MDScreen):
    pass

class AddReceivingWindow(MDScreen):
    pass

class ReceivingHomeWindow(MDScreen):
    pass

class EditProductsWindow(MDScreen):
    pass

class AddProductsWindow(MDScreen):
    pass

class ProductsHomeWindow(MDScreen):
    pass

class InventoryManagementWindow(MDScreen):
    pass

class InventoryManagement(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(1,21):
            self.ids.inventory_screen_manager.get_screen("Products Home Screen").ids.products_list.add_widget(OneLineAvatarListItem(text=f'Product {i}'))

        #for i in range(1,21):
        #    self.ids.inventory_screen_manager.get_screen("Receiving Home Screen").ids.receiving_list.add_widget(OneLineAvatarListItem(text=f'Received Inventory {i}'))

        for i in range(1,21):
            self.ids.inventory_screen_manager.get_screen("Suppliers Home Screen").ids.suppliers_list.add_widget(OneLineAvatarListItem(text=f'Suppier {i}'))
        
        '''
        self.ids.inventory_management_screen.add_widget(InventoryManagementWindow())

        self.ids.products_home_screen.add_widget(ProductsHomeWindow())
        self.ids.add_products_screen.add_widget(AddProductsWindow())
        self.ids.edit_products_screen.add_widget(EditProductsWindow())

        #self.ids.receive_inventory_home_screen.add_widget(ReceiveInventoryHomeWindow())

        self.ids.suppliers_home_screen.add_widget(SuppliersHomeWindow())
        self.ids.add_suppliers_screen.add_widget(AddSuppliersWindow())
        self.ids.edit_suppliers_screen.add_widget(EditSuppliersWindow())
        '''

    def switch_screen(self, screen_name, transition):
        self.ids.inventory_screen_manager.transition.direction = transition
        self.ids.inventory_screen_manager.current = screen_name

class InventoryApp(MDApp):
    def build(self):
        return InventoryManagement()

if __name__ == "__main__":
    InventoryApp().run()