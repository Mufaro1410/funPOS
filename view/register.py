from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from kivy.properties import ObjectProperty
from kivy.lang import Builder

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

class OpenDrawerWindow(MDScreen):
    pass

class RegisterWindow(MDBoxLayout):
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.open_drawer_screen.add_widget(OpenDrawerWindow())
        self.ids.register_main_screen.add_widget(RegisterMainWindow())
        self.ids.payment_processing_screen.add_widget(PaymentProcessingWindow())
        self.ids.payment_split_screen.add_widget(PaymentSplitWindow())
        self.ids.final_payment_processing_screen.add_widget(FinalPaymentProcessingWindow())
        self.ids.close_drawer_screen.add_widget(CloseDrawerWindow())
    '''

    def switch_screen(self, screen_name, transition):
        self.ids.register_screen_manager.transition.direction = transition
        self.ids.register_screen_manager.current = screen_name
        #self.parent.parent.ids.main_screen.children[0].ids.register.children[0].ids.register_screen_manager.transition = transition
        #self.parent.parent.ids.main_screen.children[0].ids.register.children[0].ids.register_screen_manager.current = screen_name

class RegisterApp(MDApp):
    def build(self):
        return RegisterWindow()

if __name__ == "__main__":
    RegisterApp().run()