import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

buffer = list()

class Calculator(BoxLayout):
    def acumulatevalues(self, text):
        buffer.append(text)
        print(buffer)
    def showinscreen(self, textshow):
        self.ids['lab'].text = str(textshow)

class BasicCalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    Config.set('graphics','resizable',True)
    BasicCalculatorApp().run()
