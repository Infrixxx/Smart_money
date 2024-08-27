from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
import webbrowser

class InsuranceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = FloatLayout()

        with main_layout.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
            main_layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        title_label = Label(text="Insurance Options", size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'top': 0.95}, font_size=24)
        main_layout.add_widget(title_label)

        scroll_view = ScrollView(size_hint=(0.9, 0.65), pos_hint={'center_x': 0.5, 'top': 0.7})
        self.insurance_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.insurance_layout.bind(minimum_height=self.insurance_layout.setter('height'))
        scroll_view.add_widget(self.insurance_layout)
        main_layout.add_widget(scroll_view)

        insurance_data = [
            {"name": "Discovery Insurance", "url": "https://www.discovery.co.za/"},
            {"name": "Sanlam", "url": "https://www.sanlam.co.za/"},
            {"name": "Old Mutual", "url": "https://www.oldmutual.co.za/"},
            {"name": "Liberty", "url": "https://www.liberty.co.za/"},
            {"name": "Momentum", "url": "https://www.momentum.co.za/"},
            {"name": "Auto & General", "url": "https://www.auto-general.co.za/"},
            {"name": "Dialdirect", "url": "https://www.dialdirect.co.za/"},
            {"name": "Regent Insurance", "url": "https://www.regent.co.za/"}
        ]

        for insurance in insurance_data:
            button = Button(text=insurance["name"], size_hint_y=None, height=39, background_color=(0, 0.5, 0, 1))
            button.bind(on_press=lambda instance, url=insurance["url"]: self.open_link(url))
            self.insurance_layout.add_widget(button)

        back_button = Button(text="Back", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'bottom': 0.05}, background_color=(0, 0.5, 0, 1))
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def open_link(self, url):
        webbrowser.open(url)

    def go_back(self, instance):
        self.manager.current = 'welcome'
