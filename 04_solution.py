import re

with open("04passports") as f:
    str = f.read()

passports = str.split("\n\n")
print(len(passports))

def byrvalid(v):
    return True if 1920 <= int(v.group(1)) <= 2002 else False
def iyrvalid(v):
    return True if 2010 <= int(v.group(1)) <= 2020 else False
def eyrvalid(v):
    return True if 2020 <= int(v.group(1)) <= 2030 else False
def hgtvalid(v):
    if not (match := re.match("([\d]+)(cm|in)", v.group(1))): return False
    if match.group(2) == 'cm':
        return True if 150 <= int(match.group(1)) <= 193 else False
    elif match.group(2) == 'in':
        return True if 59 <= int(match.group(1)) <= 76 else False
    else:
        return False
def hclvalid(v):
    return True if re.match(r"#[\da-f]{6}", v.group(1)) else False
def eclvalid(v):
    eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return True if v.group(1) in eyecolors else False
def pidvalid(v):
    return True if re.match(r"^\D*\d{9}\D*$", v.group(1)) else False # This is necessary as it is to guarantee that only and only 9 digits are matched


def is_pass_valid(s):
    d = {}
    properties = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]
    validators = {"byr": byrvalid, "iyr": iyrvalid, "eyr": eyrvalid, "hgt": hgtvalid, "hcl": hclvalid, "ecl": eclvalid, "pid": pidvalid}
    regex_temp = r":(#?\w+\b)"
    for prop in properties:
        pattern = prop + regex_temp
        if  match := re.search(pattern, s):
            # print(match.groups())
            if validators[prop](match):             # comment this line to get the code for the first part
                d[prop] = match.group(1)
    print(f"L={len(d)} with {d}")
    if len(d) >= 7:
        return True

if __name__ == "__main__":
    counter = 0
    for pp in passports:
        # print(pp)
        pp += '\n'
        if is_pass_valid(pp):
            counter += 1

    print(counter)
