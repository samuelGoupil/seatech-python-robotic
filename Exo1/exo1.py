import time


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    def __init__(self, nom):
        self.__name = nom

    def allumage(self):
        __power = True
        self.print_state()

    def eteindre(self):
        __power = False
        self.print_state()

    def recharge(self):
        while __battery_level <100:
            time.sleep(2)
            __battery_level = __battery_level + 10


print('salut')
walle = Robot('Walle')

print(walle.name)
