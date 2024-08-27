
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import webbrowser

class InvestmentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = FloatLayout()

        with main_layout.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
            main_layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        title_label = Label(text="Investment Platforms", size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'top': 0.95})
        main_layout.add_widget(title_label)

        platforms = [
            ("Vanguard", "https://www.vanguard.com"),
            ("Fidelity", "https://www.fidelity.com"),
            ("Charles Schwab", "https://www.schwab.com"),
            ("Robinhood", "https://www.robinhood.com"),
            ("E*TRADE", "https://www.etrade.com"),
            ("TD Ameritrade", "https://www.tdameritrade.com"),
            ("Wealthfront", "https://www.wealthfront.com"),
            ("Betterment", "https://www.betterment.com")
        ]

        button_layout = BoxLayout(orientation='vertical', size_hint=(0.9, 0.8), pos_hint={'center_x': 0.5, 'top': 0.9})
        for name, url in platforms:
            btn = Button(text=name, size_hint_y=None, height=45, background_color=(0, 0.5, 0, 1))
            btn.bind(on_press=lambda btn, url=url: self.open_url(url))
            button_layout.add_widget(btn)

        main_layout.add_widget(button_layout)

        back_button = Button(text="Back", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'bottom': 0.05}, background_color=(0, 0.5, 0, 1))
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def open_url(self, url):
        webbrowser.open(url)

    def go_back(self, instance):
        self.manager.current = 'welcome'
