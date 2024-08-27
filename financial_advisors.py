from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
import requests
import geocoder
from kivy.uix.image import Image

class FinancialAdvisorsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.api_key = 'AIzaSyCy2mp7UJwjFZNguibzz6vF5cC7GwM2Sg0'

        main_layout = FloatLayout()

        logo = Image(source='smart_money.png', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'top': 0.65})
        main_layout.add_widget(logo)

        with main_layout.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
            main_layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        location_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, 0.1), pos_hint={'center_x': 0.323, 'top': 0.95})
        location_label = Label(text="Enter Location:", size_hint=(0.4, 1))
        self.location_input = TextInput(multiline=False, size_hint=(0.6, 1))
        location_layout.add_widget(location_label)
        location_layout.add_widget(self.location_input)
        main_layout.add_widget(location_layout)

        fetch_button = Button(text="Find Advisors", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'top': 0.85}, background_color=(0, 0.5, 0, 1))
        fetch_button.bind(on_press=self.fetch_advisors)
        main_layout.add_widget(fetch_button)

        self.message_label = Label(text="", size_hint=(0.9, 0.05), pos_hint={'center_x': 0.5, 'top': 0.85})
        main_layout.add_widget(self.message_label)

        scroll_view = ScrollView(size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5, 'top': 0.7})
        self.advisors_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.advisors_layout.bind(minimum_height=self.advisors_layout.setter('height'))
        scroll_view.add_widget(self.advisors_layout)
        main_layout.add_widget(scroll_view)

        back_button = Button(text="Back", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'bottom': 0.05}, background_color=(0, 0.5, 0, 1))
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        current_location_button = Button(text="Use Current Location", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'top': 0.8}, background_color=(0, 0.5, 0, 1))
        current_location_button.bind(on_press=self.fetch_current_location)
        main_layout.add_widget(current_location_button)

        self.add_widget(main_layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def fetch_advisors(self, instance):
        location = self.location_input.text
        if not location:
            self.message_label.text = "Please enter a location."
            return

        self.search_advisors(location)

    def fetch_current_location(self, instance):
        g = geocoder.ip('me')
        if g.ok:
            location = g.city
            self.location_input.text = location
            self.search_advisors(location)
        else:
            self.message_label.text = "Unable to get current location."

    def search_advisors(self, location):
        api_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            'query': f'financial advisors in {location}',
            'key': self.api_key
        }

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()

            self.advisors_layout.clear_widgets()

            for result in data.get('results', []):
                name = result.get('name', 'No name provided')
                address = result.get('formatted_address', 'No address provided')
                place_id = result.get('place_id', '')
                advisor_label = Label(
                    text=f"Name: {name}\nAddress: {address}\nPlace ID: {place_id}",
                    size_hint_y=None,
                    height=100
                )
                self.advisors_layout.add_widget(advisor_label)

            self.message_label.text = f"Found {len(data.get('results', []))} advisors."

        except requests.RequestException as e:
            self.message_label.text = f"Error: {str(e)}"
            

    def go_back(self, instance):
        self.manager.current = 'welcome'
