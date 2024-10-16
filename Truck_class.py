from vehicle_class import Vehicle

class Truck(Vehicle):
    def __init__(self,color,has_trailer=False):
        super(). __init__(color)

        self.has_trailer = has_trailer

    def toString(self):
        return f'This vehicle is {self.getColor()}\nhas trailer:{self.has_trailer}'


if __name__ == '__main__':

    Truck1 = Truck("red")

    print(Truck1.toString())


