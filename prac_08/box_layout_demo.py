from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        """Handle the Greet button press event."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}" if name else "Hello!"

    def handle_clear(self):
        """Handle the Clear button press event."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == '__main__':
    BoxLayoutDemo().run()
