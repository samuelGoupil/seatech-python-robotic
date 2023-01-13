import time


class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
    def __init__(self, name, power=False, battery=0, speed=0):
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
            self.__battery_level = self.__battery_level + 10
            print("chargement...("+f'{self.get_battery()}'+'%)')

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
        print("Son nom est "+self.__name)
        print("Son niveau de batterie est "+f'{self.__battery_level}'+"%")
        print("Sa vitesse est de "+ f'{self.__current_speed}'+"km/h")
        if self.__power == False:
            print("Son état est : " + self.__states[0])
        else :
            print("Son état est : " + self.__states[1])

""" walle = Robot('Walle',False,0,0)

walle.get_name()
walle.get_power()
walle.allumage()
walle.get_power()
walle.get_speed()
walle.set_speed(15)
walle.get_speed()
walle.stop()
walle.get_speed()
walle.get_states()
walle.eteindre()
walle.get_states()
print(walle.get_battery())
walle.recharge()
print(walle.get_battery()) """

