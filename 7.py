


def calculate_combinations(size, combs):

	if size == 1:
		return combs
	else:
		news = []
		if len(combs)==0:
			combs.append([0])
			combs.append([1])
		else:
			for c in combs:
				n = list(c)
				n.append(0)
				news.append(n)
				n = list(c)
				n.append(1)
				news.append(n)
			combs = news
		combs = calculate_combinations(size-1,combs)
		#print(size)
		#print(combs)
		return combs

#combs = []
#combs = calculate_combinations(5, combs)
#print(combs)



def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

def is_calibrated(value,operands):
	combis = []
	combs = calculate_combinations(len(operands),combis)
	print(value, end="= ")
	for c in combs:
		total = operands[0]
		for i in range(0,len(operands)-1):
			if(c[i] == 0):
				total = total+operands[i+1]
				print("("+str(total)+"+"+str(operands[i+1]),end=")")
			if(c[i] == 1):
				total = total*operands[i+1]
				print("("+str(total)+"*"+str(operands[i+1]),end=")")
		print("Total" +str(total))

		if total == value:
			print("------------------IGUALES"+str(total))
			return True

	return False



datafile = open('input7', 'r')

array = []
for row in datafile:
	values = row.replace(":","").replace("\n","").split(" ")
	values = [int(v) for v in values]
	array.append(values)

print_array(array)

corrects=0
total = 0
for row in array:
	print(row[0])
	print(row[1:])
	if is_calibrated(row[0],row[1:]) :
		corrects = corrects + 1
		total = total + row[0]

print("Los correctos son "+str(corrects))
print("La suma es "+str(total))

