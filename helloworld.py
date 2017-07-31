numbers = [1,2,3,4,5]
strings = ["test","blabla"]
names = ["Daniel","Ann","Ellie"]

for x in xrange(0,3):
	name = names[x]
	print(name)
	print("X is"+str(x))
	x+1

print(numbers)
print(strings)
print("The final name on the names list is %s" % name)