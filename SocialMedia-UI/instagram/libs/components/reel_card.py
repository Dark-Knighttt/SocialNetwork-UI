from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

class ReelCard(MDCard):

    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    video = StringProperty()
    # post = StringProperty()
    # caption = StringProperty()
    likes = StringProperty()
    posted_ago = StringProperty()
    comments = StringProperty()
    print("Reeldoneeeeeeeeeeeeeeee")
    
    def on_press_heart(MDCard):
        likes = likes+1