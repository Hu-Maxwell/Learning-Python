class Car: 
    # the first parameter in the constructor is always named self. self refers to the object's name
    def __init__(self, model, year): 
        self.model = model
        self.year = year
        self._speed = 0
        self.__engine = "Super fast engine"

    def accelerate(self, speed_increase): 
        self._speed = self._speed + speed_increase

    def decelerate(self, speed_decrease):
        self._speed = self._speed - speed_decrease

    def brake(self):
        self._speed = 0

    def display_info(self): 
        print(f"{self.model}, {self.year}, {self._speed}, {self.__engine}")

    