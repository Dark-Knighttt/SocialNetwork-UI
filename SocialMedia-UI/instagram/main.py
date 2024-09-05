import os
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.screenmanager import MDScreenManager
# os.environ['KIVY_VIDEO'] = 'ffpyplayer'
from libs.screens.home_page import HomePage
from libs.screens.reel_page import ReelPage
from libs.screens.profile_page import ProfilePage
from libs.screens.conversation import Conversation

class MyScreenManager(MDScreenManager):
    def go_to_home(self):
        self.current = 'home'

    def go_to_reel(self):
        self.current = 'reel'
    
    def go_to_profile(self):
        self.current = 'profile'

    def go_to_chat(self):
        self.current = 'conversation'


class SocialScape(MDApp):
    def build(self):
        Window.size = [300,600]
        self.load_all_kv_files()
        sm = MyScreenManager()
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(ReelPage(name='reel'))  # Add the ReelPage screen
        sm.add_widget(ProfilePage(name='profile'))
        sm.add_widget(Conversation(name='conversation'))

        return sm
        # self.load_all_kv_files()
        # return HomePage()
    

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/appbar.kv')
        Builder.load_file('libs/components/story_creator.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/components/circular_avatar_image.kv')
        Builder.load_file('libs/components/post_card.kv')
        Builder.load_file('libs/screens/reel_page.kv')
        Builder.load_file('libs/components/reel_card.kv')
        Builder.load_file('libs/components/side_nav.kv')
        # Builder.load_file('libs/components/top_nav.kv')
        Builder.load_file('libs/screens/profile_page.kv')
        Builder.load_file('libs/screens/conversation.kv')


    def on_start(self):
        # self.root.dispatch('on_enter')
        pass



if __name__ == "__main__":
    SocialScape().run()