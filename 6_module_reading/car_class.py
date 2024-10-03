class Car: 
    # the first parameter in the constructor is always named self. self refers to the object's name
    def __init__(self, model, year): 
        self.model = model
        self.year = year
        self._speed = 0
        self.__engine = "Super fast engine"

    def speed_up(self): 
        self._speed = self._speed + 100

    def print_car_details(self): 
        print(f"{self.model}, {self.year}, {self._speed}, {self.__engine}")

    