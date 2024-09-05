from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
# from screens.home_page import HomePage
from kivymd.uix.screen import MDScreen
# from kivy.core.window import Window
from libs.screens.reel_page import ReelPage


class BottomNav(MDBoxLayout):
    avatar = StringProperty()
    # rootcolor = "000000"

    def on_press_home(MDScreen):
        print("it worked")

    def on_press_reel(MDScreen):
        return ReelPage()

# class Reel(MDScreen):
#     def build(self):
#         Window.size = [300,600]
#         return ReelPage()