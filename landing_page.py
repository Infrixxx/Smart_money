from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
import os

KV = '''
ScreenManager:
    MainScreen:
    NextScreen:

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: 40

        MDLabel:
            text: "Smart Money"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0, 0.5, 0, 1  # Dark green color
            font_style: 'H2'

        Image:
            source: 'smart_money.png'
            size_hint: (0.5, 0.3)
            pos_hint: {'center_x': 0.5}
            allow_stretch: True
            keep_ratio: True

        MDLabel:
            text: "Be smart with your money"
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0, 0.5, 0, 1  # Dark green color
            font_style: 'Subtitle1'

        MDRaisedButton:
            text: "Next"
            size_hint: (0.5, 0.1)
            pos_hint: {'center_x': 0.5}
            md_bg_color: 0, 0.5, 0, 1  # Green background color
            on_release: app.root.current = 'next'

<NextScreen>:
    name: 'next'
    BoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: 40

        MDLabel:
            text: "Welcome to the next page!"
            halign: 'center'
     
'''

class MainScreen(Screen):
    pass

class NextScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MainApp().run()
