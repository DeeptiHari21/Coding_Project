import json


class parking_lot:
    """Creates a virtual parking lot based on input size of the lot."""

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
    """Class to take the license plate number and park the car in a spot."""

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

    def park(self, spot_number, parking_array):
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
                car.park(spot_number, parked_cars)
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
                print("The parking is:", lot.json_map(spots, cars))
                with open("parking.json", "w") as outfile:
                    outfile.write(lot.json_map(spots, cars))
                sys.exit("Parking lot is full.")
        if len(car_list) == 0:
            print("The parking is:", lot.json_map(spots, cars))
            with open("parking.json", "w") as outfile:
                outfile.write(lot.json_map(spots, cars))
            sys.exit("All cars parked!")


if __name__ == "__main__":
    main()
