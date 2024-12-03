import csv
import operator
datafile = open('input1', 'r')

def count_value(value, l):
	return l.count(value)



data1 = []
data2 = []
for row in datafile:
	elems = row.split("   ")
	print("Elems="+str(elems))
	print(elems[0] +"--"+elems[1])
	data1.append(int(elems[0]))
	data2.append(int(elems[1]))    

counts = list(map(lambda x: count_value(x, data2),data1))
print(counts)
total = sum(list(map(operator.mul,counts,data1)))
print(total)


#total = list(map(operator.sub, data1, data2))

#total = list(map(abs, total))
