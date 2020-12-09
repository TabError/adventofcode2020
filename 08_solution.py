import re

with open("08data") as f:
    data = f.read()

program = [(c, int(d)) for c, d in re.findall(r"(jmp|nop|acc) ([\+-]\d+)", data)]
# program = [(i, match[0], int(match[1])) for i, match in enumerate(re.findall(r"(jmp|acc) ([\+-]\d+)", data))]


class LoopError(Exception):
    pass

##### the instructions as functions #####
def jmp(i: int):
    global line; line += i
def acc(i: int):
    global acc; acc += i
    global line; line += 1
def nop(i: int):
    global line; line += 1

instruction_set = {"acc": acc, "jmp": jmp, "nop": nop}




##### part one #####
def try_program():
    print(f"We are in {line=}")
    if line in already_visited:
        return acc
    already_visited.add(line)
    command, argument = program[line]
    instruction_set[command](argument)
    return try_program()

already_visited = set()
acc = 0; line = 0
res = try_program()
print(f"{res=}")


##### part two iterative #####
command_conversion = {"acc": "acc", "jmp": "nop", "nop": "jmp"}

def try_modified_program():
    if line in already_visited:
        raise LoopError
    elif len(program) == line:
        return acc
    already_visited.add(line)
    command, argument = program[line]
    instruction_set[command](argument)
    return try_modified_program()

already_visited = set()
acc = 0; line = 0
while True:
    already_visited.add(line)
    original_command, argument = program[line]
    command = command_conversion[original_command]
    # print(f"before {line=} {command=} {argument=} {acc=}")
    if original_command in ["jmp", "nop"]:
        tmp_already_visited = already_visited
        tmp_line = line
        tmp_acc = acc
        try:
            print(f"Try changing {line=}")
            instruction_set[command](argument)
            try_modified_program()
            print("We have finally found the path")
            print(f"We changed {tmp_line=} {original_command=} {argument=} {tmp_acc=}")
            break;
        except LoopError:
            print(f"changing {tmp_line=} leads to a loop at {line}")
            pass
        line = tmp_line
        acc = tmp_acc
        already_visited = tmp_already_visited
    instruction_set[original_command](argument)
    # print(f"after  {line=} {command=} {argument=} {acc=}")

print(f"{acc=}")
