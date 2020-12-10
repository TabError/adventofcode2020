with open("09data") as f:
    data = [int(i) for i in f.read().splitlines()]

########## part one ##########
def initialize_field(length: int):
    l = []
    for i in range(length - 1):
        l.append([])
        for j in range(i+1,length):
            l[i].append(data[i] + data[j])
    return l

def update_field(field: list, new_index: int):
    field.pop(0)
    for i in range(len(field)):
        field[i].append(data[new_index - (len(field)+1) + i] + data[new_index])
    field.append([data[new_index - 1] + data[new_index]])

def is_in_field(field: list, number: int):
    return True if number in [i for subl in field for i in subl] else False

len_preamble = 25
possible_sums = initialize_field(len_preamble)
idx = len_preamble
while is_in_field(possible_sums, data[idx]):
    update_field(possible_sums, idx)
    idx += 1

not_sum = data[idx]
print(f"{not_sum=} at index {idx=}")

########## part two ##########
def find_sequence(s):
    i=0; j=0
    global id
    seq_sum = data[i]
    while True:
        if seq_sum < s: j += 1; seq_sum += data[j]
        if seq_sum > s: seq_sum -= data[i]; i += 1
        if seq_sum == s: break
    return i,j


start, end = find_sequence(not_sum)
print(f"Sequence starts at {start} until {end}")

res = min(data[start:end+1]) + max(data[start:end+1])
print(f"Sum of the smallest and largest nums in sequence is {res}")
