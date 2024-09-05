from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

class SideNav(MDBoxLayout):
    avatar = StringProperty()
    likes = StringProperty()
    posted_ago = StringProperty()
    comments = StringProperty()
    