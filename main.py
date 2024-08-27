from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from landing_screen import LandingScreen
from options_screen import OptionsScreen
from budget import BudgetScreen
from financial_advisors import FinancialAdvisorsScreen
from insurance import InsuranceScreen
from investment_platforms import InvestmentScreen

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LandingScreen(name='hello'))
        sm.add_widget(OptionsScreen(name='welcome'))
        sm.add_widget(BudgetScreen(name='budget'))
        sm.add_widget(FinancialAdvisorsScreen(name='financial_advisors'))
        sm.add_widget(InsuranceScreen(name='insurance'))
        sm.add_widget(InvestmentScreen(name='investment_options'))
        return sm

if __name__ == '__main__':
    MyApp().run()
