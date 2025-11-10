from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (360, 600)

class CalculatorGrid(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0]
        self.spacing = 5

        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=40,
            size_hint=(1, None),
            height=110,
            background_color=(0.12, 0.12, 0.12, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[10, 10],
        )
        self.add_widget(self.display)

        # Grid tombol 4 kolom
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        button_grid = GridLayout(cols=4, size_hint=(1, 1), spacing=5, padding=[10, 10, 10, 10])
        for row in buttons:
            for label in row:
                button = Button(
                    text=label,
                    font_size=32,
                    background_color=(0.15, 0.15, 0.15, 1),
                    color=(1, 1, 1, 1),
                    size_hint=(1, 1)
                )
                button.bind(on_press=self.on_button_press)
                button_grid.add_widget(button)

        self.add_widget(button_grid)

        del_btn = Button(
            text='Del',
            font_size=24,
            size_hint=(1, None),
            height=60,
            background_color=(0.6, 0.15, 0.15, 1),
            color=(1, 1, 1, 1)
        )
        del_btn.bind(on_press=self.on_button_press)
        self.add_widget(del_btn)

        self.expression = ""

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.expression = ""
        elif text == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        elif text == "Del":
            self.expression = self.expression[:-1]
        else:
            self.expression += text

        self.display.text = self.expression


class CalculatorApp(App):
    def build(self):
        self.title = "Kalkulator"
        return CalculatorGrid()


if __name__ == "__main__":
    CalculatorApp().run()
