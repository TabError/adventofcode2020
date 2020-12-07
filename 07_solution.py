import re

with open("07bags") as f:
    rules = f.readlines()

rules = [r.replace('.\n', '') for r in rules]

pattern = re.compile("(.*?) bags contain (.*)")
rules = [pattern.match(r) for r in rules]

def listed_containers(con):
    """listed_containers(included_bags : str)
    returns [(amount1, name1), (amount2, name2), ...]
    Gets a string representing the bags included"""
    if con == "no other bags":
        return []
    con = [re.match(r"(\d*) (.*?) bags?", c) for c in con.split(", ")]
    return [(c.group(1), c.group(2)) for c in con]

all_bags = {match.group(1):listed_containers(match.group(2)) for match in rules}


########## in hw many bags can shiny gold be in ##########
def big_bags(bag, all, other_parents = []):
    for big, littles in all.items():
        if bag in [name for nums, name in littles] and big not in other_parents:
            other_parents.append(big)
            big_bags(big, all, other_parents)
    return other_parents

our_bag = "shiny gold"
greater_bags = big_bags(our_bag, all_bags)
print(len(greater_bags))


########## how many bags have to be in shinygold ##########
def num_little_bags(bag, all):
    """gets """
    return sum([int(quantity) + int(quantity) * num_little_bags(b, all) for quantity, b in all[bag]])

our_bag = "shiny gold"
smaller_bags = num_little_bags(our_bag, all_bags)
print(smaller_bags)
