"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor
#from EpuckMotors import EpuckMotors



class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)

class SmashRobotMotors():
    def __init__(self) -> None:
        self.__back_left_wheel__joint = RobotMotor('back_left_wheel_joint')
        self.__back_right_wheel__joint = RobotMotor('back_right_wheel_joint')
        self.__front_left_wheel__joint = RobotMotor('front_left_wheel_joint')
        self.__front_right_wheel__joint = RobotMotor('front_right_wheel_joint')

    
    def go_right(self):
        self.__back_left_wheel__joint.setVelocity(15)
        self.__back_right_wheel__joint.setVelocity(-15)
        self.__front_left_wheel__joint.setVelocity(15)
        self.__front_right_wheel__joint.setVelocity(-15)
        
    def go_left(self):
        self.__back_left_wheel__joint.setVelocity(-5)
        self.__back_right_wheel__joint.setVelocity(15)
        self.__front_left_wheel__joint.setVelocity(-5)
        self.__front_right_wheel__joint.setVelocity(15)

    def go_front(self):
        self.__back_left_wheel__joint.setVelocity(10)
        self.__back_right_wheel__joint.setVelocity(10)
        self.__front_left_wheel__joint.setVelocity(10)
        self.__front_right_wheel__joint.setVelocity(10)

    def go_back(self):
        self.__back_left_wheel__joint.setVelocity(-5)
        self.__back_right_wheel__joint.setVelocity(-5)
        self.__front_left_wheel__joint.setVelocity(-5)
        self.__front_right_wheel__joint.setVelocity(-5)
    
class Robotfighter(Robot):
    def __init__(self):
        super().__init__()
        self.motors=SmashRobotMotors()

    def go_left(self):
        self.motors.go_left()

    def go_right(self):
        self.motors.go_right()

    def go_front(self):
        self.motors.go_front()

    def go_back(self):
        self.motors.go_back()

    
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
    pass


# Enter here exit cleanup code.
