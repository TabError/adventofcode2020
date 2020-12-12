import itertools
import copy

with open("11data") as f:
    data = f.read().splitlines()
# with open("11test") as f:
#     data = f.read().splitlines()

########## global variables ##########
data = [list(s) for s in data]
rows = len(data)
cols = len(data[0])
orientations = [(i,j) for i,j in itertools.product([-1,0,1], repeat=2) if i != 0 or j != 0]

########## functions ##########
def part_one(data):
    area = data[:]
    sight = False
    tolerance = 3
    area = simulate_round(area, tolerance, sight)
    occupied_seats = sum([s.count('#') for s in area])
    print(f"{occupied_seats=}")

def part_two(data):
    area = data[:]
    sight = True
    tolerance = 4
    area = simulate_round(area, tolerance, sight)
    occupied_seats = sum([s.count('#') for s in area])
    print(f"{occupied_seats=}")

def simulate_round(area_before, tolerance_max, sight):
    area_after = copy.deepcopy(area_before)
    for i in range(rows):
        for j in range(cols):
            if area_before[i][j] == '.':
                area_after[i][j] = '.'
            elif area_before[i][j] == 'L':
                area_after[i][j] = '#' if occupied_adjacent_seats(area_before, i, j, rec=sight) <= 0 else 'L'
            elif area_before[i][j] == '#':
                area_after[i][j] = '#' if occupied_adjacent_seats(area_before, i, j, rec=sight) <= tolerance_max else 'L'
            else:
                print(f"Wow, here is an unknown Symbol in the area: ({i}, {j})")
    # print(area_after)
    return area_after if area_after == area_before else simulate_round(area_after, tolerance_max, sight)

def occupied_adjacent_seats(area, x, y, rec=False):
    neighbours = [adjacent_seat(area, x, y, i, j, recursive=rec) for i,j in orientations]
    neighbours = [tup for tup in neighbours if tup != None]
    return sum([1 for i,j in neighbours if area[i][j] == '#'])

def adjacent_seat(area, x, y, x_inc, y_inc, recursive=False):
    x_suc = x+x_inc; y_suc = y+y_inc
    if 0 <= x_suc < rows and 0 <= y_suc < cols:
        if area[x_suc][y_suc] in ['#', 'L']:
            return (x_suc, y_suc)
        else:
            return adjacent_seat(area, x_suc, y_suc, x_inc, y_inc, recursive) if recursive else None
    else:
        return None

########## main ##########
if __name__ == "__main__":
    part_one(data)
    part_two(data)
