with open("06declarations") as f:
    input = f.read()

input = input.split("\n\n")
partone = [i.replace("\n", '') for i in input]
parttwo = [i.split("\n") for i in input]

########## partone ##########
sets = [set(s) for s in partone]
nums = [len(s) for s in sets]
total = sum(nums)
print(total)

########## parttwo ##########
common_letters = [[c for c in l[0] if all([c in s for s in l[1:None]]) ] for l in parttwo]
nums = [len(l) for l in common_letters]
total = sum(nums)
print(total)
