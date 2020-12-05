with open("05seats") as f:
    seats = f.readlines()

seats = [s.replace('\n', '') for s in seats]

highest_seat = 0
lowest_seat = 2**10
id_list = []
binDict = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
for s in seats:
    id = 0
    expo = 1
    for c in s[-1::-1]:
        id += binDict[c] * expo
        expo *= 2
    print(f"seat: {s} has id {id}")
    if id > highest_seat:
        highest_seat = id
    if id < lowest_seat:
        lowest_seat = id
    id_list.append(id)

print(f"{highest_seat=}")
print(f"{lowest_seat=}")
for i in range(lowest_seat, highest_seat+1):
    if i not in id_list:
        print(f"{i} is not in the id_list")
