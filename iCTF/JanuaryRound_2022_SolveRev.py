'''
import string
import numpy as np
from secret import pt

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index

pt_chunks = [pt[i:i+2] for i in range(0, len(pt), 2)]

ct = ""
enc = np.matrix(((1,0), (6,11)))
for chunk in pt_chunks:
    mult = ( enc * np.matrix(([int(values[chunk[0]])], [int(values[chunk[1]])])) ) % 26
    for key, value in values.items():
        if value == mult.item(0):
            ct += key
    for key, value in values.items():
        if value == mult.item(1):
            ct += key

print(f"{ct = }")
# ct = 'NYWDRCDQIJGLHASMIXHQFCUVFQNWTUOTCMLK'
'''



import string
import numpy as np

enc  = "NYWDRCDQIJGLHASMIXHQFCUVFQNWTUOTCMLK"
flag = "ictf{"

values = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values[letter] = index

pt_chunks = [enc[i:i+2] for i in range(0, len(enc), 2)]

for chunk in pt_chunks:
	flag += chunk[0]
	poz1 = values[chunk[0]]
	poz2 = values[chunk[1]]
	i = 0
	while(1):
		if (poz1 * 6 + 11 * i ) % 26 == poz2:
			break;
		i = i+1
	rev = ''
	for key, value in values.items():
		if value == i:
			rev = key

	flag += rev



flag+='}'
print(flag)