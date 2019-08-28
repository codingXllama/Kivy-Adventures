from kivy.app import App
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self):
        return Button(text='Welcome to the App', background_color=(0, 10, 1, 1), font_size=50)


if __name__ == "__main__":
    SimpleApp().run()
