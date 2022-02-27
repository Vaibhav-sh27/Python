import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.button import Label
class HelloKivy(App):
    def build(self):
        return Label(text='[color = ff0000][b]Hello[/b] kivy[/color]',font_size ='20sp',markup = True)
hello = HelloKivy()
hello.run()