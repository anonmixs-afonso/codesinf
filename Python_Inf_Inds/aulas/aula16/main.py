import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.core.window import Window

buffer = list()
class Calculator(BoxLayout):
    def acumulatevalues(self, text):
        buffer.append(text)
        print(buffer)
    def showinscreen(self, textshow):
        self.ids['lab'].text = " ".join(map(str,buffer))
    def calculate(self):
        if (len(buffer) > 0):
            try:
                self.ids['lab'].text =  str(eval(''.join(buffer)))
            except Exception as args:
                self.ids['lab'].text =  'Invalid Operation'
    def delete (self):
        if (len(buffer) > 0):
            sizel = len(buffer)
            sizeel = len(buffer[0])
            numel = sizel/sizeel
            buffer.pop(int(numel-1))
            self.ids['lab'].text = " ".join(map(str,buffer))
    def ac (self):
        if (len(buffer) > 0):
            buffer.clear()
            self.ids['lab'].text = '0'
class BasicCalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    Window.size = (600, 400)
    Config.set('graphics','resizable',True)
    BasicCalculatorApp().run()

