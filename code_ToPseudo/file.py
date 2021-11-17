seconds = 1

def start():
    move(0)
    move(-90)
    move(-180)
    move(90)

def move(degres):
    chassis_ctrl.move_with_time(degres,seconds)