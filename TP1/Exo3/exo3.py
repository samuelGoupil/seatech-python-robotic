from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    _name="DEFAULT"

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def setName(self,name):
        self._name = name
    
    def getName(self):
        return("I am a "+self._name)




class AerialVehicle(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class GroundVehicle(metaclass=ABCMeta):
    @abstractmethod
    def moove(self):
        pass

class UnderseaVehicle(metaclass=ABCMeta):
    @abstractmethod
    def navigate(self):
        pass

class UAV(UnmannedVehicle, AerialVehicle):
    def start(self):
        print("I'm ready to fly")

    def stop(self):
        print("I had landed")

    def fly(self):
        print("I'm flying")

class UUV(UnmannedVehicle, UnderseaVehicle):
    def start(self):
        print("I'm ready to navigate")

    def stop(self):
        print("I'm docked")

    def navigate(self):
        print("I'm swimming")

class UGV(UnmannedVehicle, GroundVehicle):
    def start(self):
        print("I'm ready to moove")

    def stop(self):
        print("I had stop mooving")

    def moove(self):
        print("I'm mooving")


if __name__ == '__main__':

    uav = UAV()
    uav.setName("plane")
    print(uav.getName())
    uav.start()
    uav.stop()
    uav.fly()

    ugv = UGV()
    ugv.setName("rover")
    print(ugv.getName())
    ugv.start()
    ugv.stop()
    ugv.moove()

    uuv = UUV()
    uuv.setName("submarine")
    print(uuv.getName())
    uuv.start()
    uuv.stop()
    uuv.navigate()

