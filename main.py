# imports
import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.properties import ColorProperty
from random import random


# configs
Config.set('graphics', 'resizable', 1)

def rand_color():
    color_list = []
    for i in range(1,17):
        color_list.append([random() for i in range(3)] + [1])
    return color_list

# layout class
class CalcGridLayout(GridLayout):
    
    # calculator functions
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


        

# Necessary app class
class CalculatorApp(App):
    color_list = rand_color()

    def build(self):
        return CalcGridLayout()
    
# creating object and running it
calcApp = CalculatorApp()
calcApp.run()