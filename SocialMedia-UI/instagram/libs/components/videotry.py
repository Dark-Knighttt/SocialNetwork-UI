from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    Video:
        id: video
        source: 'assets/images/ganeshji.mp4'
        state: 'play'
        options: {'eos': 'loop'}
        size_hint: (1, 0.8)

    # MDRaisedButton:
    #     text: 'Play'
    #     on_release: app.play_video()
    
    # MDRaisedButton:
    #     text: 'Pause'
    #     on_release: app.pause_video()
    
    # MDRaisedButton:
    #     text: 'Stop'
    #     on_release: app.stop_video()
'''

class VideoPlayerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def play_video(self):
        video = self.root.ids.video
        video.state = 'play'

    def pause_video(self):
        video = self.root.ids.video
        video.state = 'pause'

    def stop_video(self):
        video = self.root.ids.video
        video.state = 'stop'
        video.seek(0)  # Seek to the start

if __name__ == '__main__':
    VideoPlayerApp().run()
