from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @property
    @abstractmethod
    def start(self):
        pass

    @property
    @abstractmethod
    def stop(self):
        pass



class AerialVehicle(metaclass=ABCMeta):
    @property
    @abstractmethod
    def fly(self):
        pass

class GroundVehicle(metaclass=ABCMeta):
    @property
    @abstractmethod
    def moove(self):
        pass

class UnderseaVehicle(metaclass=ABCMeta):
    @property
    @abstractmethod
    def navigate(self):
        pass

class UAV(AerialVehicle):
    def fly(self):
        print("I'm flying")

class UUV(UnderseaVehicle):
    def navigate(self):
        print("I'm swimming")

class UGV():
    def moove(self):
        print("I'm mooving")


uav = UAV()
uav.do_something_interesting()
uav.do_something_aerial_specific()

ugv = UGV()
ugv.do_something_interesting()
ugv.do_something_ground_specific()

uuv = UUV()
uuv.do_something_interesting()
uuv.do_something_undersea_specific()