class MusicPlayable:  # class Mixin
    def play_music(self, song):
        print(f"Now is playing {song} song....")


class Car(MusicPlayable):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print("I can drive")

    def __str__(self):
        return f"Model: {self.model} year: {self.year}"


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print("I can drive using electic engine")

    def __str__(self):
        return super(ElectricCar, self).__str__() + f" battery: {self.battery}"


class FuelCar(Car):
    __total_fuel = 5000

    @staticmethod
    def fuel_type():
        return "AI - 95"

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f"I can drive using fuel engine {self.model}")

    def __str__(self):
        return super(FuelCar, self).__str__() + f" fuel_bank: {self.fuel_bank}"

    def __gt__(self, other):
        return self.__fuel_bank > other.__fuel_bank and self.year > other.year

    def __lt__(self, other):
        return self.__fuel_bank < other.__fuel_bank and self.year < other.year

    def __le__(self, other):
        return self.__fuel_bank <= other.__fuel_bank and self.year <= other.year

    def __eq__(self, other):
        return self.__fuel_bank == other.__fuel_bank and self.year == other.year

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, fuel_bank, battery):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectricCar.__init__(self, model, year, battery)


class SmartPhone(MusicPlayable):
    pass


print(str(FuelCar.get_total_fuel()) + f" liters ({FuelCar.fuel_type()})")

prius = HybridCar("Toyota Prius", 2020, 60, 80000)
print(prius)
prius.drive()
prius.play_music("Beatles - Yesterday")
iphone = SmartPhone()
iphone.play_music("La la la")
print(HybridCar.__mro__)
print(HybridCar.mro())

bmw = FuelCar("BMW M5", 2021, 90)
print(bmw)
num1 = 89
num2 = 50
print(num1 > num2)
print(prius > bmw)
print(bmw > prius)

print(prius + bmw)
print(str(FuelCar.get_total_fuel()) + f" liters ({FuelCar.fuel_type()})")
