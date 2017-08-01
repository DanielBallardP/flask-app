import numpy as np
numbers = [1,2,3,4,5]
strings = ["test","blabla"]
names = ["Daniel","Ann","Ellie"]

np_numbers = np.array(numbers)
np_strings = np.array(strings)
np_names = np.array(names)

for x in range(0,3):
	name = names[x]
	print(name)
	print("X is"+str(x))
	x+1

print(np.mean(np_numbers))
print(np_strings[3])
print(np_names[:])
print(type(np_names))
print("The final name on the names list is %s" % name)
