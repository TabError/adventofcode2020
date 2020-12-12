with open("11data") as f:
    data = f.read().splitlines()
# with open("11test") as f:
#     data = f.read().splitlines()

# global variables
area = [list(s) for s in data]
rows = len(area)
cols = len(area[0])

########## part one ##########
def adjacent_seats(x, y):
    lower_x = max([0, x-1])
    lower_y = max([0, y-1])
    higher_x = min([x+1, rows-1])
    higher_y = min([y+1, cols-1])
    adjacent = {(lower_x, lower_y),
                (lower_x, y),
                (lower_x, higher_y),
                (x, lower_y),
                (x, higher_y),
                (higher_x, lower_y),
                (higher_x, y),
                (higher_x, higher_y)}
    adjacent -= {(x, y)}
    return adjacent

def seat_accessible(x, y):
    for i, j in adjacent_seats(x, y):
        if area[i][j] == '#':
            return False
    return True

def seat_tooCrowded(x, y):
    occ = 0
    for i, j in adjacent_seats(x, y):
        if area[i][j] == '#':
            occ += 1
    return True if occ >= 4 else False

def simulate_round():
    becomes_occupied = set()
    becomes_empty = set()
    for i in range(rows):
        for j in range(cols):
            if area[i][j] == 'L' and seat_accessible(i, j):
                becomes_occupied.add((i,j))
            if area[i][j] == '#' and seat_tooCrowded(i,j):
                becomes_empty.add((i, j))
    for i, j in becomes_empty:
        area[i][j] = 'L'
    for i, j in becomes_occupied:
        area[i][j] = '#'
    return len(becomes_empty | becomes_occupied)

while n := simulate_round(): print(f"Number of seats changed state: {n=}")
occupied_seats = sum([s.count('#') for s in area])
print(f"{occupied_seats=}")

########## part two ##########
area = [list(s) for s in data]
rows = len(area)
cols = len(area[0])

#overwrite adjacent method
def seeable_seat(x,y, x_inc, y_inc):
    if x + x_inc < 0 or rows-1 < x + x_inc or y + y_inc < 0 or cols-1 < y + y_inc:
        return None
    elif area[x + x_inc][y + y_inc] in ['L', '#']:
        return (x + x_inc, y + y_inc)
    else:
        return seeable_seat(x + x_inc, y + y_inc, x_inc, y_inc)

def adjacent_seats(x, y):
    adjacent = set()
    adjacent.add(seeable_seat(x,y, x_inc = -1, y_inc = -1))
    adjacent.add(seeable_seat(x,y, x_inc = -1, y_inc = 0))
    adjacent.add(seeable_seat(x,y, x_inc = -1, y_inc = 1))
    adjacent.add(seeable_seat(x,y, x_inc = 0 , y_inc = -1))
    adjacent.add(seeable_seat(x,y, x_inc = 0 , y_inc = 1))
    adjacent.add(seeable_seat(x,y, x_inc = 1 , y_inc = -1))
    adjacent.add(seeable_seat(x,y, x_inc = 1 , y_inc = 0))
    adjacent.add(seeable_seat(x,y, x_inc = 1 , y_inc = 1))
    adjacent -= {None}
    return adjacent

# overwrite with 5 or more instead of 4 or more
def seat_tooCrowded(x, y):
    occ = 0
    for i, j in adjacent_seats(x, y):
        if area[i][j] == '#':
            occ += 1
    return True if occ >= 5 else False

while n := simulate_round(): print(f"Number of seats changed state: {n=}")
occupied_seats = sum([s.count('#') for s in area])
print(f"{occupied_seats=}")
