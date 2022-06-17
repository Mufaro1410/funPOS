from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineAvatarListItem

from kivy.lang import Builder

import os

dirname = os.path.dirname(__file__)

Builder.load_file(os.path.join(dirname, "reports.kv"))

class EditDrawerReportsWindow(MDScreen):
    pass

class DrawerReportsWindow(MDScreen):
    pass

class EditInventoryReportsWindow(MDScreen):
    pass

class InventoryReportsWindow(MDScreen):
    pass

class EditSalesReportsWindow(MDScreen):
    pass

class SalesReportsWindow(MDScreen):
    pass
        
        

class ReportsMainWindow(MDScreen):
    pass

class ReportsWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(1,21):
            self.ids.reports_screen_manager.get_screen("Sales Reports Screen").ids.sales_reports_list.add_widget(OneLineAvatarListItem(text=f'Sale {i}'))

        for i in range(1,21):
            self.ids.reports_screen_manager.get_screen("Drawer Reports Screen").ids.drawer_reports_list.add_widget(OneLineAvatarListItem(text=f'Drawer {i}'))

        '''
        self.ids.reports_main_screen.add_widget(ReportsMainWindow())

        self.ids.sales_reports.add_widget(SalesReportsWindow())
        self.ids.edit_sales_reports.add_widget(EditSalesReportsWindow())

        self.ids.inventory_reports.add_widget(InventoryReportsWindow())
        self.ids.edit_inventory_reports.add_widget(EditInventoryReportsWindow())

        self.ids.drawer_reports.add_widget(DrawerReportsWindow())
        self.ids.edit_drawer_reports.add_widget(EditDrawerReportsWindow())
        '''

    def switch_screen(self, screen_name, transition):
        self.ids.reports_screen_manager.transition.direction = transition
        self.ids.reports_screen_manager.current = screen_name

class ReportsApp(MDApp):
    def build(self):
        return ReportsWindow()

if __name__ == "__main__":
    ReportsApp().run()