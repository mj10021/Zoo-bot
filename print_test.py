#Derek Zoolander robot
# servo 0 is right motor, servo 1 is left motor
#SetupServo(0)
#SetupServo(1)

RIGHT = 1
LEFT = 3


#function to turn either 90* or 270* right
def turn(right_or_left):

    if right_or_left != RIGHT or right_or_left != LEFT:
        right_or_left = 0

    #turns 90* either 0, 1, or 3 times depending on input
    for x in xrange(right_or_left):
        print "%s" % str(int(current_speed) - 20)
        time.sleep(100)
        print "%s" % str(current_speed)
        time.sleep(100)


#function to control manual steering of robot
def steer(new_angle):
    if 134 < int(new_angle) < 181:
        new_angle = steer_angle
        if steer_angle > 0:
            print "%s" % str(steer_angle)
    elif "x" == new_angle:
        exit(1)
    #else:
        #pass


#function to spin in circles for a user defined time
def dance_for(milliseconds):
    print "%s" % str(180 - int(current_speed))
    time.sleep(milliseconds)
    print "%s" str(current_speed)


#run for ever
while(true):

    current_speed = 90

    print "%s" str(current_speed)
    print "%s" str(current_speed)

    mode_selection = raw_input("Press 's' to set speed, 'r' to turn right,\
     'l' to turn left, 'b' to breakdance,\
      'm' to steer manually, or 'x' to exit:")

    #sets speed to given int
    if "s" == mode_selection:
        new_speed = raw_input("Set forward speed 90-180:")
        if 89 < int(new_speed) < 181:
            int(new_speed) = current_speed
            print("Speed set to %s." % str(current_speed))

        #checks for 'x' to exit
        elif "x" == new_speed:
            exit(1)
        else:
            print("Is %s in between 90 and 180, Hansel." % str(new_speed))

        #turns 90* using the turn function
        elif "r" == mode_selection:
            turn(RIGHT)

        #turns 270* using the turn function
        elif "l" == mode_selection:
            turn(LEFT)

        elif "b" == mode_selection:
            dance_duration = raw_input("How long do you want me to dance for?")
            if int(dance_duration) > 0:
                dance_for(int(dance_duration))
            else:
                print("I can't dance for %s, Hansel." % str(dance_duration))

        #accepts manual speed selection on motor 1
        elif "m" == mode_selection:
            new_angle = raw_input("Set turn speed from 180-135:")
            if 134 < new_angle < 181:
                steer(int(new_angle))
            else:
                print("Is %s in between 135 and 180, Hansel." % str(new_angle))

        #checks for 'x' to exit
        elif "x" == mode_selection:
            print("Relax.")
            exit(1)

        #if someone does not select a real option, yell at them!
        else:
            print("Cool story, Hansel.")
