def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def newJump():
    while (front_is_clear()):
        move()

    while (wall_in_front()):
        turn_left()

        while (front_is_clear()):
            move()

        turn_right()
        move()
        turn_right()

        while (front_is_clear()):
            move()

        turn_left()


while at_goal() == False:
    newJump()
