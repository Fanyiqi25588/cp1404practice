from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    output_km = StringProperty("0.0")

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ Handle calculation (triggered by text input change) """
        value = self.get_validated_miles()
        self.output_km = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        """
        Handle Up/Down button press, update text input with new value, call calculation function
        :param change: the amount to change
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        Get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0


MilesConverterApp().run()
