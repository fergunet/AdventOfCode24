import csv
import operator
datafile = open('input1', 'r')


data1 = []
data2 = []
for row in datafile:
	elems = row.split("   ")
	print("Elems="+str(elems))
	print(elems[0] +"--"+elems[1])
	data1.append(int(elems[0]))
	data2.append(int(elems[1]))    

print(data1)
data1.sort()
data2.sort()

total = list(map(operator.sub, data1, data2))
print(total)
total = list(map(abs, total))
total = sum(total)
print(total)
