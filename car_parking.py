import json


class parking_lot:
    """Creates a virtual parking lot based on input size of the lot:
    Create a parking lot class that takes in a square footage size as input and creates an array of empty values based on the input square footage size. Assume every parking spot is 8x12 (96 ft2) for this program, but have the algorithm that calculates the array size be able to account for different parking spot sizes. For example, a parking lot of size 2000ft2 can fit 20 cars, but if the parking spots were 10x12 (120 ft2), it could only fit 16 cars. The size of the array will determine how many cars can fit in the parking lot. Further create a method for the parking lot class that maps vehicles to parked spots in a JSON object. Call this method at the end of the program, and save the object to a file."""

    def __init__(self):
        """Takes input for the area of the parking lot. Sets the dimensions of the lot to 8x12 if no input is entered."""
        self.size = float(input("Parking area:"))
        self.width = float(input("Width of each spot (default 8):") or 8)
        self.length = float(input("Length of each spot (default 12):") or 12)

    def spots(self):
        """Calculates the number of parking spots and returns as an array."""
        number_of_spots = int(self.size / (self.length * self.width))
        parking_spots = [None] * number_of_spots
        return parking_spots

    def json_map(self, spots_list, vehicle_number_list):
        spots = spots_list
        vehicles = vehicle_number_list
        map_spots_vehicles = dict(zip(spots, vehicles))
        return json.dumps(dict(sorted(map_spots_vehicles.items())))


class license:
    """Class to take the license plate number and park the car in a spot:
    Create a car class that takes in a 7 digit license plate and sets it as a property. The car will have 2 methods:
    1. A magic method to output the license plate when converting the class instance to a string.
    2. A "park" method that will take a parking lot and spot # as input and fill in the selected spot in the parking lot. If another car is parked in that spot, return a status indicating the car was not parked successfully. If no car is parked in that spot, return a status indicating the car was successfully parked."""

    def __init__(self, license_number):
        license_number = str(license_number)
        self._license_number = license_number

    @property
    def license_number(self):
        """Takes in the license plate number and converts it to string."""
        return self._license_number

    @license_number.setter
    def license_number(self, num):
        num = str(num)
        if len(num) != 7:
            print("Not a 7-digit number")
        else:
            self._license_number = num

    def park(self, lot_number, spot_number, parking_array):
        """Takes in parking lot and spot number and fill it."""
        if spot_number > len(parking_array):
            print("Parking not so big")
        else:
            if parking_array[spot_number] == None:
                parking_array[spot_number] = self.license_number
                # print('Car successfully parked!')
            elif parking_array[spot_number] != None:
                # print('Car not parked.')
                pass
        return parking_array


from random import randint
import sys


def main():
    """Main function:
    Have a main method take an array of cars with random license plates and have them park in a random spot in the parking lot array until the input array is empty or the parking lot is full. If a car tries to park in an occupied spot, have it try to park in a different spot instead until it successfully parks. Once the parking lot is full, exit the program. Output when a car does or does not park successfully to the terminal (Ex. "Car with license plate [LICENSE_PLATE] parked successfully in spot [SPOT #]")."""
    lot = parking_lot()
    parking_spots = lot.spots()
    parked_cars = [None] * len(parking_spots)
    number_of_cars = randint(0, 25)
    car_list = [randint(1000000, 9999999) for i in range(number_of_cars)]
    car = license(0000000)
    spots = []
    cars = []
    while len(parking_spots) != 0:
        while len(car_list) != 0:
            spot_number = randint(0, len(parked_cars) - 1)
            if parked_cars[spot_number] == None:
                car.license_number = car_list[0]
                car.park(1, spot_number, parked_cars)
                print(
                    f"Car with license plate number {car.license_number} is parked in spot {spot_number}."
                )
                parked_cars[spot_number] = car_list[0]
                spots.append(spot_number)
                cars.append(car_list[0])
                car_list.pop(0)
                parking_spots.pop(0)
            elif parked_cars[spot_number] != None:
                pass
            if len(parking_spots) == 0:
                if len(car_list) != 0:
                    print("Cars", car_list, "are not parked.")
                print("The parking order is:", lot.json_map(spots, cars))
                with open("./parking.json", "w") as outfile:
                    outfile.write(lot.json_map(spots, cars))
                sys.exit("Parking lot is full.")
        if len(car_list) == 0:
            print("The parking order is:", lot.json_map(spots, cars))
            with open("./parking.json", "w") as outfile:
                outfile.write(lot.json_map(spots, cars))
            sys.exit("All cars parked!")


if __name__ == "__main__":
    main()
