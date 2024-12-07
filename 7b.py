
#Esta es la versión correcta, que no tiene en cuenta la preferencia de operadores

def calculate_combinations(size, combs):

	if size == 1:
		return combs
	else:
		news = []
		if len(combs)==0:
			combs.append([0])
			combs.append([1])
			combs.append([2])
		else:
			for c in combs:
				n = list(c)
				n.append(0)
				news.append(n)
				n = list(c)
				n.append(1)
				news.append(n)
				n = list(c)
				n.append(2)
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

def reduce_operands(operands,c):
	new_operands = []
	new_combs = []
	new_operands.append(operands[0])
	for i in range(0,len(operands)-1):
		if(c[i] == 2):
			old = new_operands[-1]
			new = operands[i+1]
			oldnew = str(old)+str(new)
			new_operands[-1]=int(oldnew)
		else:
			new_combs.append(c[i])
			new_operands.append(operands[i+1])

	return new_operands,new_combs

def apply_comb(operands,c):
	total = operands[0]
	for i in range(0,len(operands)-1):
		if(c[i] == 0):
			total = total+operands[i+1]
			#print("("+str(total)+"+"+str(operands[i+1]),end=")")
		if(c[i] == 1):
			total = total*operands[i+1]
			#print("("+str(total)+"*"+str(operands[i+1]),end=")")
		if(c[i] == 2):
			#old = operands[i]
			new = operands[i+1]
			oldnew = str(total)+str(new)
			total =int(oldnew)
	#print("Total" +str(total))
	return total

def is_calibrated(value,operands):
	combis = []
	combs = calculate_combinations(len(operands),combis)
	print("-------------Value: "+str(value))
	1==1
	for c in combs:
		#print("COMB:"+str(c))
		#print("OPER:"+str(operands))
		total = apply_comb(operands,c)
		#print("---")
		#print("Total" +str(total))

		if total == value:
			#print("------------------IGUALES"+str(total))
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

