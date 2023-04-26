class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1
        print(type(self))

    @staticmethod
    def RobotInstances():
        return Robot.__counter


if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(y.RobotInstances())
    print(Robot.RobotInstances())
