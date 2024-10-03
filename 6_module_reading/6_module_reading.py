from car_class import Car


if __name__ == "__main__":
    my_car = Car("Lamborghini", 8024)

    Car.display_info(my_car)

    Car.accelerate(my_car, 200)
    Car.display_info(my_car)

    Car.decelerate(my_car, 100)
    Car.display_info(my_car)

    Car.brake(my_car)
    Car.display_info(my_car)
