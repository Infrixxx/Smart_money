from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle

class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.income = 0
        self.total_expenses = 0
        self.expenses = []

        main_layout = FloatLayout()

        with main_layout.canvas.before:
            Color(0.0, 0.5, 0.0, 1)
            self.bg_rect = Rectangle(size=main_layout.size, pos=main_layout.pos)
            main_layout.bind(size=self._update_bg_rect, pos=self._update_bg_rect)

        income_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'top': 0.9})
        income_label = Label(text="Enter Income (ZAR):", size_hint=(0.4, 1))
        self.income_input = TextInput(multiline=False, size_hint=(0.6, 1))
        income_layout.add_widget(income_label)
        income_layout.add_widget(self.income_input)
        main_layout.add_widget(income_layout)

        update_income_button = Button(text="Set Income", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.25, 'top': 0.75})
        update_income_button.bind(on_press=self.update_income)
        main_layout.add_widget(update_income_button)

        self.remaining_label = Label(text="Remaining Income: R0", size_hint=(0.9, 0.05), pos_hint={'center_x': 0.5, 'top': 0.8})
        main_layout.add_widget(self.remaining_label)

        scroll_view = ScrollView(size_hint=(0.9, 0.4), pos_hint={'center_x': 0.5, 'top': 0.7})
        self.expenses_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.expenses_layout.bind(minimum_height=self.expenses_layout.setter('height'))
        scroll_view.add_widget(self.expenses_layout)
        main_layout.add_widget(scroll_view)

        add_expense_layout = BoxLayout(orientation='horizontal', size_hint=(0.9, 0.1), pos_hint={'center_x': 0.5, 'y': 0.2})
        self.item_input = TextInput(hint_text="Item", multiline=False, size_hint=(0.6, 1))
        self.price_input = TextInput(hint_text="Price (ZAR)", multiline=False, input_filter='float', size_hint=(0.4, 1))
        add_expense_layout.add_widget(self.item_input)
        add_expense_layout.add_widget(self.price_input)
        main_layout.add_widget(add_expense_layout)

        add_expense_button = Button(text="Add Expense", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.75, 'y': 0.1})
        add_expense_button.bind(on_press=self.add_expense)
        main_layout.add_widget(add_expense_button)

        clear_expenses_button = Button(text="Clear Expenses", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.25, 'y': 0.1})
        clear_expenses_button.bind(on_press=self.clear_expenses)
        main_layout.add_widget(clear_expenses_button)

        back_button = Button(text="Back", size_hint=(0.4, 0.05), pos_hint={'center_x': 0.5, 'bottom': 0.05})
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        self.add_widget(main_layout)

    def _update_bg_rect(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def update_income(self, instance):
        try:
            self.income = float(self.income_input.text)
            self.update_remaining_income()
        except ValueError:
            self.income_input.text = "0"
            self.income = 0
            self.update_remaining_income()

    def update_remaining_income(self):
        remaining_income = self.income - self.total_expenses
        self.remaining_label.text = f"Remaining Income: R{remaining_income:.2f}"

    def add_expense(self, instance):
        try:
            item = self.item_input.text
            price = float(self.price_input.text)

            if item and price:
                self.total_expenses += price
                self.expenses.append((item, price))

                expense_label = Label(text=f"{item}: R{price:.2f}", size_hint_y=None, height=40)
                self.expenses_layout.add_widget(expense_label)

                self.update_remaining_income()

                self.item_input.text = ""
                self.price_input.text = ""
        except ValueError:
            self.price_input.text = ""

    def clear_expenses(self, instance):
        self.total_expenses = 0
        self.expenses.clear()
        self.expenses_layout.clear_widgets()
        self.update_remaining_income()

    def go_back(self, instance):
        self.manager.current = 'welcome'
