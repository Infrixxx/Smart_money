from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class LandingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = FloatLayout()
        
        with layout.canvas.before:
            Color(1, 1, 1, 1) 
            self.bg_rect = Rectangle(size=layout.size, pos=layout.pos)
            layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        title_label = Label(
            text='Smart Money',
            font_size=Window.width * 0.1,
            color=(0.0, 0.5, 0.0, 1), 
            size_hint=(None, None),
            size=(Window.width * 0.8, Window.height * 0.15),
            pos_hint={'center_x': 0.5, 'top': 0.85}
        )
        layout.add_widget(title_label)

        image = Image(
            source='smart_money.png',
            size_hint=(None, None),
            size=(Window.width * 0.3, Window.height * 0.4),
            pos_hint={'center_x': 0.5, 'center_y': 0.55}
        )
        layout.add_widget(image)

        slogan_label = Label(
            text='Be smart with your money',
            font_size=Window.width * 0.05,
            color=(0.0, 0.5, 0.0, 1),
            size_hint=(None, None),
            size=(Window.width * 0.8, Window.height * 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.25}
        )
        layout.add_widget(slogan_label)

        options_button = Button(
            text='Options',
            background_color=(0.0, 0.5, 0.0, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(Window.width * 0.4, Window.height * 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1}
        )
        options_button.bind(on_press=self.go_to_options)
        layout.add_widget(options_button)

        self.add_widget(layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def go_to_options(self, instance):
        self.manager.current = 'welcome'