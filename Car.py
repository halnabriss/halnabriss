
class Car:
    def __init__(self, brand, color, drive_wheels, model):
        self.brand = brand
        self.color = color
        self.drive_wheels = drive_wheels
        self.model = model


    def findAge(self):
        return 2022-int(self.model)
