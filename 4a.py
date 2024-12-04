

def print_array(array):
	for i in range(0,len(array)):
		for j in range(0,len(array[i])):
			print(array[i][j],end='')
		print()

def xcounter(i,j,matrix):
	if(matrix[i-1][j-1]=="M" and matrix[i+1][j-1]=="M" and matrix[i-1][j+1]=="S" and matrix[i+1][j+1]=="S"):
		return 1
	if(matrix[i-1][j-1]=="S" and matrix[i+1][j-1]=="S" and matrix[i-1][j+1]=="M" and matrix[i+1][j+1]=="M"):
		return 1
	if(matrix[i-1][j-1]=="M" and matrix[i+1][j-1]=="S" and matrix[i-1][j+1]=="M" and matrix[i+1][j+1]=="S"):
		return 1
	if(matrix[i-1][j-1]=="S" and matrix[i+1][j-1]=="M" and matrix[i-1][j+1]=="S" and matrix[i+1][j+1]=="M"):
		return 1
	return 0

	


array = []

datafile = open('input4', 'r')

for row in datafile:
	l = list(row)
	l = l[:-1]
	array.append(l)

print_array(array)


founds = 0
for i in range(1,len(array)-1):
	print("Fila "+str(array[i]))
	for j in range(1,len(array[i])-1):
		print(array[i][j])
		if (array[i][j] == "A"):
			print("buscando "+str(i)+"-"+str(j))			
			founds = founds + xcounter(i,j,array)
	print()
print(founds)
	

