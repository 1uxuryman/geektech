class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Cow:
    pass


class Animal:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        if isinstance(address, Address):
            self.__address = address
        else:
            raise AttributeError('Attribute address must be of type Address')
        self.__is_born()

    def set_age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise AttributeError('Wrong value for age attribute it must be positive number')
        else:
            self.__age = value

    def get_age(self):
        return self.__age

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_address(self, value):
        if isinstance(value, Address):
            self.__address = value
        else:
            raise AttributeError('Attribute address must be of type Address')

    def get_address(self):
        return self.__address

    def __is_born(self):
        print(f"Animal {self.__name} was born")

    def info(self):
        return f"Name: {self.__name} age: {self.__age} \n" \
               f"Adrress of animal: {self.__address.city}, " \
               f"{self.__address.street} {self.__address.number}"

    def speak(self):
        raise NotImplementedError("Method speak must be implemented")


class Dog(Animal):
    def __init__(self, name, age, commands, addrees):
        super(Dog, self).__init__(name, age, addrees)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f"\nCommands: {self.commands}"

    def speak(self):
        print("Gav gav")


class Cat(Animal):
    def __init__(self, name, age, addrees):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age, addrees)

    def speak(self):
        print("Myau myau")


class Fish(Animal):
    def __init__(self, name, age, addrees):
        # super().__init__(name, age)
        super(Fish, self).__init__(name, age, addrees)

    def speak(self):
        print('Bul bul')


# animal = Animal("Animal 1", 8, None)
# animal.set_age(4)  # animal.name = -12
# print(f"Name: {animal.get_name()} age: {animal.get_age()}")

address_of_tom = Address("NY", "Wall Street", 2221)
# address_of_tom.set_address("LA")
address_of_tom.city = "LA"
tom_cat = Cat("Tom", 2, address_of_tom)
snoopy_dog = Dog("Snoopy", 3, "Sit", Address("Bishkek", "Toktogula", 21))
freddy_fish = Fish("Freddy", 5, Address("London", "Bayker Street", 45))

animals_list = [freddy_fish, tom_cat, snoopy_dog]
for animal in animals_list:
    print(animal.info())
    animal.speak()
