from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with higher fares due to fanciness."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the total fare including flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return string representation of SilverServiceTaxi with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
