"""
Exam 2 resit.
"""
class Car:
    """
    Exercise 4. You have to import the class, not to copy it.
    """

    car_type = None  # marka auta.
    horse_power = None
    color = None

    def __init__(self, car_type, horse_power, color):
        self.car_type = car_type
        self.horse_power = horse_power
        self.color = color

    def describe(self):
        """
        Dumps car's data.
        """
        return "Car: {}, horse power: {}, color: {}".format(self.car_type,
                                                            self.horse_power,
                                                            self.color)
