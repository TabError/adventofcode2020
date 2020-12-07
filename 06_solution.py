with open("06declarations") as f:
    data = f.read()

data = data.split("\n\n")

########## partone ##########
partone = [i.replace("\n", '') for i in data]
sets = [set(s) for s in partone]
nums = [len(s) for s in sets]
total = sum(nums)
print(total)

########## parttwo ##########
parttwo = [i.split("\n") for i in data]
common_letters = [[c for c in l[0] if all([c in s for s in l[1:None]]) ] for l in parttwo]
nums = [len(l) for l in common_letters]
total = sum(nums)
print(total)

########## parttwo again ##########
common_letters = [set.intersection(*[set(s) for s in l]) for l in parttwo]
nums = [len(l) for l in common_letters]
total = sum(nums)
print(total)

########## parttwo again ##########
from functools import reduce
common_letters = [reduce(set.intersection, [set(s) for s in l]) for l in parttwo]
nums = [len(l) for l in common_letters]
total = sum(nums)
print(total)
