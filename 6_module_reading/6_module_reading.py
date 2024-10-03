from car_class import Car


if __name__ == "__main__":
    my_car = Car("Lamborghini", 8024)

    Car.display_info(my_car)

    my_car.accelerate(200)
    Car.display_info(my_car)

    my_car.decelerate(100)
    Car.display_info(my_car)

    my_car.brake()
    Car.display_info(my_car)
