from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import json
from libs.components.reel_card import ReelCard


class ReelPage(MDScreen):

    profile_picture = "libs/screens/avatar.jfif"

    def on_enter(self, *args):
        super().on_enter(*args)
        self.list_reels()

    def list_reels(self):
        with open('instagram/assets/data/reels.json') as f_obj:
            data = json.load(f_obj)
            for reel in data['reels']:
                self.ids.reels_container.add_widget(ReelCard(
                    username=reel['username'],
                    avatar=reel['avatar'],
                    video=reel['video'],
                    likes=reel['likes'],
                    comments=reel['comments'],
                    posted_ago=reel['posted_ago']
                ))


