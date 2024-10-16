from garage_class import Garage
from Truck_class import Truck

class GarageTester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):

        Truck1 = Truck('black',False) # Creating a truck object to put in the Garage

        garage = Garage() # Creating the garage 

        garage.setVehicle(Truck1) # Storing the Truck object in the garage using the setVehicle method

        return garage.toString() # For displaying the vehicle description

if __name__ == '__main__':

    garageTester = GarageTester()

    print(garageTester.getExample())