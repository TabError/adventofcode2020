with open("10data") as f:
    data = [int(line) for line in f]

# print(f"{data=}")
# print(len(data))

########## part one ##########
def jolt_diffs(adapters: list):
    adapters += [0, max(adapters)+3]
    adapters.sort()
    one = 0; three = 0
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:        one += 1
        elif adapters[i+1] - adapters[i] == 3:      three += 1
        else:                                       print(f"{i=}, {adapters[i+1] - adapters[i]=}")
    return one, three

one_jolt_diff, three_jolt_diff = jolt_diffs(data.copy())
# print(f"{one_jolt_diff=} {three_jolt_diff=}")
result = one_jolt_diff * three_jolt_diff
print(f"{result=}")


########## part two ##########
def one_series(adapters: list):
    adapters += [0, max(adapters)+3]
    adapters.sort()
    series = []
    i = 0; series_length = 0
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 1:
            series_length += 1
        if adapters[i+1] - adapters[i] == 3:
            series.append(series_length)
            series_length = 0
        i += 1
    return series

def tribonacci(length: int):
    tri = [1,1,2]
    while len(tri) <= length:
        tri.append(tri[len(tri)-1] + tri[len(tri)-2] + tri[len(tri)-3])
    return tri

list_of_one_series = one_series(data.copy())
# print(f"{list_of_one_series=}")
tribonacci_series = tribonacci(max(list_of_one_series))
# print(f"{tribonacci_series=}")

import math
result = math.prod([tribonacci_series[ones] for ones in list_of_one_series])
print(f"{result=}")
