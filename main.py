from kivy.app import App
from kivy.uix.label import Label

class MonApp(App):
    def build(self):
        return Label(text="Application de Gestion")

if __name__ == "__main__":
    MonApp().run()
