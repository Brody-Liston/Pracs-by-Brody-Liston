"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main(fuel=None):
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    my_car.car_name = "Ford GT"

    # -----------------------------------------------------------------#
    limo = Car(100)  # add a limo car, with 100 fuel
    limo.car_name = "Chrysler 300 Limo"
    # -----------------------------------------------------------------#
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)

    print(my_car)


    # -----------------------------------------------------------------#
    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)   # print the Car limo's details
    print(limo)

    # -----------------------------------------------------------------#
    limo.add_fuel(20) # add 20 fuel to the limo using add_fuel method
    # -----------------------------------------------------------------#
    print("fuel =", limo.fuel)
    # -----------------------------------------------------------------#
    limo.drive(115)  # drive the car 155km
    print("fuel =", limo.fuel)   # display the fuel and odometer
    print("odo =", limo.odometer)
    print(limo)
    # -----------------------------------------------------------------#



    # -----------------------------------------------------------------#

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))



main()