with open("09data") as f:
    data = [int(i) for i in f.read().splitlines()]

def initial_field():
    l = []
    for i in range(24):
        l.append([])
        for j in range(i+1,24+1):
            l[i].append(data[i] + data[j])
    return l

def update_field(field: list, new_index: int):
    field.pop(0)
    for i in range(23):
        field[i].append(data[new_index - 24 + i] + data[new_index])
    field.append([data[new_index - 1] + data[new_index]])

def is_in_field(field: list, number: int):
    return True if number in [i for subl in field for i in subl] else False


possible_sums = initial_field()

x = 25
while True:
    num = data[x]
    if not is_in_field(possible_sums, num):
        break
    update_field(possible_sums, x)
    x += 1

not_sum = data[x]
print(f"{not_sum=} at index {x=}")

def sequence_sums(s):
    for i in range(len(data)):
        seq_sum = 0
        for j in range(i, len(data)):
            seq_sum += data[j]
            if seq_sum > s:
                break
            elif seq_sum == s:
                return i, j

start, end = sequence_sums(not_sum)
print(f"Sequence starts at {start} until {end}")

res = min(data[start:end+1]) + max(data[start:end+1])
print(f"Sum of the smallest and largest nums in sequence is {res}")
