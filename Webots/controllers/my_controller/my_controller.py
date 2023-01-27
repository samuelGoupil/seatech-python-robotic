"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, DistanceSensor, GPS
#from EpuckMotors import EpuckMotors



class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class SmashRobotMotors():
    def __init__(self) -> None:
        self.__left_wheel__motor = RobotMotor('left wheel motor')
        self.__right_wheel__motor = RobotMotor('right wheel motor')

    
    def go_right(self):
        self.__left_wheel__motor.setVelocity(15)
        self.__right_wheel__motor.setVelocity(-15)
        
        
    def go_left(self):
        self.__left_wheel__motor.setVelocity(-15)
        self.__right_wheel__motor.setVelocity(15)
        

    def go_front(self):
        self.__left_wheel__motor.setVelocity(10)
        self.__right_wheel__motor.setVelocity(10)
        

    def go_back(self):
        self.__left_wheel__motor.setVelocity(-5)
        self.__right_wheel__motor.setVelocity(-5)


class RobotGPS(GPS):
    def __init__(self, samplingPeriod):
        super().__init__('gps')
        self.enable(int(samplingPeriod))



class Sensor(DistanceSensor):
    def __init__(self) -> None:
        self.__front_letf__sensor = DistanceSensor('cliff_front_left')
        self.__front_right__sensor = DistanceSensor('cliff_front_right')
        self.__letf__sensor = DistanceSensor('cliff_left')
        self.__right__sensor = DistanceSensor('cliff_right')


        
    
class Robotfighter(Robot):
    def __init__(self):
        super().__init__()
        self.motors=SmashRobotMotors()
        self.gps=RobotGPS(self.getBasicTimeStep())
        my_position=self.gps.getValues()

    def go_left(self):
        self.motors.go_left()

    def go_right(self):
        self.motors.go_right()

    def go_front(self):
        self.motors.go_front()

    def go_back(self):
        self.motors.go_back()
    
    def get_myPosition(self):
        print(self.get_myPosition)


        
    

    
fa=Robotfighter()
timestep = int(fa.getBasicTimeStep())

fa.go_right()
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while fa.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    print(fa.gps.getCoordinateSystem())
    print(fa.gps.getValues())
    print("espace")
    fa.get_myPosition()
    pass


# Enter here exit cleanup code.
