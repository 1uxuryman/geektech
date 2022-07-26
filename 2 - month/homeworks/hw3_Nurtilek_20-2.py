class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'cpu: {self.cpu}, memory: {self.memory}, {self.make_computations()}'

    def __eq__(self, other):
        return self.memory == other

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - Beeline')

    def __str__(self):
        return f"Sim cards: {self.sim_cards_list} "

Phone.sim_cards_list = ['Beeline, Megacom, Oshka']

class SmartPhone(Computer, Phone):

    def __init__(self, location, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.location = location

    def __eq__(self, other):
        return self.memory == other

    def use_gps(self, location):
        print(f'{location} to "bishkek park"')

    def __str__(self):
        return f'ваше место положение{self.location}'


new_computer = Computer(12, 512)
new_phone = Phone(1).call(1 , 996777668844)
new_smartphone = SmartPhone(' geektech', 4, 256, 'Oshka')
new_smartphone2 = SmartPhone(' geekstudio', 8, 512, 'Beelane')
print(new_computer)
print(new_smartphone)
print(new_smartphone2)
print(new_smartphone.use_gps('geektech'))
print(new_computer == new_smartphone)



