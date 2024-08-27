from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from landing_screen import LandingScreen
from options_screen import OptionsScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingScreen(name='hello'))
        sm.add_widget(OptionsScreen(name='welcome'))
        return sm

if __name__ == '__main__':
    MyApp().run()
