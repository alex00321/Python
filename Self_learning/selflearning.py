from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def polygon(t, n, length):
    angle = 360.0/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)
polygon(bob,7,70)
print(bob)
wait_for_user()