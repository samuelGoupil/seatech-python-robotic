import time


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    def __init__(self, name, power, battery, speed):
        self.__name = name
        self.__power = power
        self.__battery_level = battery
        self.__current_speed = speed
        

    def allumage(self):
        print("switch on")
        self.__power = True
        
       

    def eteindre(self):
        print("switch off")
        self.__power = False
        
       

    def recharge(self):
        while self.__battery_level < 100:
            time.sleep(0.1)
            self.__battery_level = self.__battery_level + 1
            print(self.get_battery())

    def get_name(self):
        print("Le robot s'appelle " + self.__name) 

    def get_power(self):
        if self.__power == False :
            print('OFF')
        else : 
            print('ON')

    def get_battery(self):
        return self.__battery_level

    def set_speed(self, speed):
        self.__current_speed = speed
    
    def get_speed(self):
        print('La vitesse du robot est de '+f'{self.__current_speed}' +'km/h')

    def stop(self):
        self.__current_speed = 0
        print('le robot est arreté')

    def get_states(self):
        if self.__power == False:
            print(self.__states[0])
        else :
            print(self.__states[1])

walle = Robot('Walle',False,0,0)

print(walle.get_name())
print(walle.get_power())
walle.allumage()
print(walle.get_power())
print(walle.get_speed())
walle.set_speed(15)
print(walle.get_speed())
walle.stop()
print(walle.get_speed())
print(walle.get_states())
walle.eteindre()
print(walle.get_states())






""" print(walle.get_battery())
walle.recharge()
print(walle.get_battery()) """

