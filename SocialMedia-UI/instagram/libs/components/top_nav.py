from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty


class TopNav(MDBoxLayout):
    avatar = StringProperty()
    username = StringProperty()