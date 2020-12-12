with open("12data") as f:
    data = f.read().splitlines()

########## global variables ##########
cardinal_points = ['N', 'E', 'S', 'W']

########## functions ##########
def part_one(instructions, x_pos=0, y_pos=0):
    direction = 90
    for command, argument in instructions:
        if command == 'F':
            command = cardinal_points[int(direction/90) % 4]
        if command in ['L', 'R']:
            direction += (1 if command == 'R' else -1) * argument
        elif command == 'N':
            y_pos += argument
        elif command == 'E':
            x_pos += argument
        elif command == 'S':
            y_pos -= argument
        elif command == 'W':
            x_pos -= argument
        else:
            print(f"ALERT: unknown instruction!!!")
    return x_pos, y_pos


def part_two(instructions, x_pos=0, y_pos=0, x_waypoint=0, y_waypoint=0):
    direction=0
    for command, argument in instructions:
        if command == 'F':
            x_pos += x_waypoint*argument
            y_pos += y_waypoint*argument
        elif command in ['L', 'R']:
            x_waypoint, y_waypoint = rotate(x_waypoint, y_waypoint, argument, command)
        elif command == 'N':
            y_waypoint += argument
        elif command == 'E':
            x_waypoint += argument
        elif command == 'S':
            y_waypoint -= argument
        elif command == 'W':
            x_waypoint -= argument
        else:
            print(f"ALERT: unknown instruction!!!")
    return x_pos, y_pos

def rotate(x, y, degree, clockwise=1):
    if clockwise in ['L', 'R']:
        clockwise = True if clockwise == 'R' else False
    rots = int(degree/90)%4
    for i in range(rots):
        x, y =  y if clockwise else -y, -x if clockwise else  x
    return x, y

########## main ##########
if __name__ == "__main__":
    data = [(d[:1], int(d[1:])) for d in data]

    x_end, y_end = part_one(data)
    manhatten_dist = abs(x_end) + abs(y_end)
    print(f"{manhatten_dist=}")

    x_end, y_end = part_two(data, x_waypoint=10, y_waypoint=1)
    manhatten_dist = abs(x_end) + abs(y_end)
    print(f"{manhatten_dist=}")
