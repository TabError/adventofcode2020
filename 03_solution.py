import numpy as np

map = []
with open("03trees") as f:
    map = f.readlines()

x = len(map[0]) - 1
y = len(map)
arr = np.empty((y, x), np.int8)

def sym_to_num(c):
    return 0 if c == '.' else 1 if c == '#' else -1

for i, r in enumerate(map):
    for j, c in enumerate(r[0:-1]):
        arr[i][j] = sym_to_num(c)

print(arr)


slopes = [[1,1,0],[1,3,0],[1,5,0],[1,7,0],[2,1,0]]

def slope_encounter(tuple):
        i=0; j=0
        counter = 0
        while(i < arr.shape[0]):
            if arr[i][j%arr.shape[1]] == 1:
                counter += 1
            i += tuple[0]
            j += tuple[1]
        tuple[2] = counter

prod = 1
for s in slopes:
    slope_encounter(s)
    prod *= s[2]

print(slopes)
print(prod)
