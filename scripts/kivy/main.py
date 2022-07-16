from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel

Window.clearcolor = (0, 33 / 255, 71 / 255, 1)


class Translator(App):
    def build(self):
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=40,
                            spacing=10,
                            padding=10
                            )
        self.INPUT = TextInput(text='Enter text to learn')
        self.OUTPUT = TextInput(text='list to learn ')
        submit = Button(text='Translate', on_press=self.submit)
        layout.add_widget(self.INPUT)
        layout.add_widget(self.OUTPUT)
        layout.add_widget(submit)
        return layout

    def submit(self, obj):
        print(self.INPUT.text)
        self.OUTPUT.text = self.INPUT.text + 'changed'


Translator().run()
