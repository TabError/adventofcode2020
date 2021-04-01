

def part_one(t, ids):
    waiting_minutes = [loop_time - t%loop_time for loop_time in ids]
    least_waiting = min(waiting_minutes)
    print(f"{min(waiting_minutes)=}")

    result = ids[waiting_minutes.index(least_waiting)] * least_waiting
    print(f"{result=}")

def part_two():
    pass


if __name__=="__main__":
    with open("13data") as f:
        timestamp = int(f.readline())
        busses  = [int(x) for x in f.readline().replace('\n', '').split(',') if not x == 'x']

    part_one(timestamp, busses)
    part_two()
