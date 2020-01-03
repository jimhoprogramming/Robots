#qpy:kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()
