class Transport:
    '''Transport is abstract class for inharitance'''
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        super().__init__(the_model, the_year, the_color)  # constructor matching


class Car(Transport):
    wheels = 4  # class attributes

    def __init__(self, the_model, the_year, the_color, the_penalties=0):  # constructor
        super().__init__(the_model, the_year, the_color)
        self.penalties = the_penalties  # self.model attribute

    def drive(self, city):  # method of a class
        print(f'Car {self.model} is driving to {city}')


class Truck(Car): # Inharitance
    wheels = 10
    def __init__(self, the_model, the_year, the_color, the_penalties, load_capacity):
        super().__init__(the_model, the_year, the_color, the_penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, cargo_type, weight):
        if self.load_capacity >= weight:
            print(f'Cargo of {cargo_type} was loaded on truck {self.model}')
        else:
            print(f'Sorry this truck can load only {self.load_capacity}')


print(f'We need {20 * Car.wheels} winter lastics')

mazda_car = Car('Mazda RX-7', 2020, 'Green')
print(mazda_car)
print(f"Model: {mazda_car.model} year: {mazda_car.year} color: {mazda_car.color} "
      f"penalties: {mazda_car.penalties} wheels: {mazda_car.wheels}")

# bmw_car - object reference, referenced variable
bmw_car = Car(the_model='BMW 7', the_color='Black', the_year=2000, the_penalties=1000)
print(f"Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} "
      f"penalties: {bmw_car.penalties} wheels: {bmw_car.wheels}")

mazda_car.drive('Osh')
bmw_car.drive('Bishkek')
bmw_car.change_color('Yellow')
bmw_car.wheels = 5
print(f"Model: {bmw_car.model} year: {bmw_car.year} color: {bmw_car.color} "
      f"penalties: {bmw_car.penalties} wheels: {bmw_car.wheels}")

Car.wheels = 5

honda_car = Car('Honda Pilot', 2021, 'Silver')
print(f"Model: {honda_car.model} year: {honda_car.year} color: {honda_car.color} "
      f"penalties: {honda_car.penalties} wheels: {honda_car.wheels}")

airbus = Plane("Boeng 747", 2022, "White")
print(f"Model of plane: {airbus.model} year: {airbus.year} color: {airbus.color}")

man_truck = Truck('Man 90', 2019, 'Red', 2500, 28000)
print(f"Model of truck: {man_truck.model} year: {man_truck.year} color: {man_truck.color} "
      f"penalties: {man_truck.penalties} wheels: {man_truck.wheels} "
      f"load capacity: {man_truck.load_capacity}")
man_truck.load_cargo('Wheal', 25000)
print(Transport.__doc__)