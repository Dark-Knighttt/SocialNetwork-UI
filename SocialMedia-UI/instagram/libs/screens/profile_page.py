from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout

class ProfilePage(MDScreen):
    profile_picture = "libs/screens/avatar.jfif"

class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass