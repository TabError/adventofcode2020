import re

l=[]
with open("02passwords") as f:
	pattern = r"^([0-9]+)-([0-9]+) (.*?): (.*)$"
	#pattern = re.compile(pattern)
	for line in f:
		l.append(re.search(pattern, line))


print("found matches: {}".format(len(l)))


def isvalid(match):
	a = int(match[0])
	b = int(match[1])
	c = match[2]
	s = match[3]
	
	i = len(re.findall(c, s))
	
	if a <= i <= b:
		return True
	else:
		return False

l = [m for m in l if type(m) == re.Match]
print("without None: {}".format(len(l)))

v = [m for m in l if isvalid(m.groups())]
print("and valid: {}".format(len(v)))


def realValidation(match):
	a = int(match[0])
	b = int(match[1])
	c = match[2]
	s = match[3]
	
	
	return True if (s[a-1] == c or s[b-1] == c) and not (s[a-1] == s[b-1]) else False

rv = [m for m in l if realValidation(m.groups())]
print("really valid: {}".format(len(rv)))


