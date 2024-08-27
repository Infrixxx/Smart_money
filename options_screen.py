from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout

class OptionsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = FloatLayout()

        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # Set background color to white
            self.bg_rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
            main_layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        image = Image(
            source='smart_money.png',
            size_hint=(0.2, 0.3),
            pos_hint={'center_x': 0.5, 'top': 1}
        )
        main_layout.add_widget(image)

        button_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.8, 0.5), pos_hint={'center_x': 0.5, 'y': 0.35})

        buttons = ['Budget', 'Insurance', 'Financial Advisors', 'Investment']
        for button_text in buttons:
            button = Button(
                text=button_text,
                background_color=(0.0, 0.5, 0.0, 1),
                color=(1, 1, 1, 1),
                size_hint=(1, None),
                height=50
            )
            button.bind(on_press=lambda instance, bt=button_text: self.go_to_screen(bt))
            button_layout.add_widget(button)

        main_layout.add_widget(button_layout)

        back_button = Button(
            text='Back',
            background_color=(0.0, 0.5, 0.0, 1),
            color=(1, 1, 1, 1),
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.3, 'y': 0.1}
        )
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def go_to_screen(self, button_text):
        screen_map = {
            'Budget': 'budget',
            'Insurance': 'insurance',
            'Financial Advisors': 'financial_advisors',
            'Investment': 'investment_options'
        }
        self.manager.current = screen_map.get(button_text, 'options')

    def go_back(self, instance):
        self.manager.current = 'hello' 

    def go_to_financial_advisors(self, instance):
        self.manager.current = 'financial_advisors'