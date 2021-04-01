import numpy as np
import re

l = []
with open("01nums") as f:
	pat = r"[0-9]+"
	l = re.findall(pat, f.read())
	l = [int(s) for s in l]

print(len(l))

print("results:")
for i in l:
	for j in l:
		for k in l:
			if i+j+k == 2020:
				print("{i} * {j} * {k} = {0}".format(i*j*k, i=i, j=j, k=k))


def foo():
	print("hello")
	shortString = "Garden" * 3
	print(shortString)



foo()
