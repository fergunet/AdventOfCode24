

def print_array(array):
	for i in range(0,len(array)):
		for j in range(0,len(array[i])):
			print(array[i][j],end='')
		print()

def horizontals(i,j,matrix,word):
	hors = 0
	#To right
	print("RIGHT")
	if((j+len(word)) > len(matrix[i])):
		print("Te sales por la derecha")
	else:
		foundR = True
		for c in range(0,len(word)):
			print(str(i)+"-"+str(j+c))
			print(matrix[i][j+c]+"=="+word[c])
			if matrix[i][j+c] != word[c]:
				foundR = False
				print("not equal")
		if foundR:
			print("Encontrada derecha")
			hors = hors + 1
	#To left
	print("LEFT")
	if(((j+1)-len(word)) < 0):
		print("Te sales por la izquierda")
	else:
		foundL = True
		for c in range(0,len(word)):
			print(str(i)+"-"+str(j-c))
			print(matrix[i][j-c]+"=="+word[c])
			if matrix[i][j-c] != word[c]:
				foundL = False
				print("not equal")
		if foundL:
			print("Encontrada izquierda")
			hors = hors + 1
	return hors
	
def verticals(i,j,matrix,word):
	vers = 0
	#To down
	print("DOWN")
	print(str(i+len(word)) +" "+ str(len(matrix)))
	if((i+len(word)) > len(matrix)):
		print("Te sales por abajo")
	else:
		foundD = True
		for c in range(0,len(word)):
			print(str(i+c)+"-"+str(j))
			print(matrix[i+c][j]+"=="+word[c])
			if matrix[i+c][j] != word[c]:
				foundD = False
				print("not equal")
		if foundD:
			print("Encontrada abajo")
			vers = vers + 1
	#To up
	print("UP")
	if(((i+1)-len(word)) < 0):
		print("Te sales por arriba")
	else:
		foundU = True
		for c in range(0,len(word)):
			print(str(i-c)+"-"+str(j))
			print(matrix[i-c][j]+"=="+word[c])
			if matrix[i-c][j] != word[c]:
				foundU = False
				print("not equal")
		if foundU:
			print("Encontrada arriba")
			vers = vers + 1
	return vers


def diagonals_up(i,j,matrix,word):
	dups = 0
	#To right
	print("UP RIGHT")
	if((j+len(word)) > len(matrix[i]) or ((i+1)-len(word)) < 0):
		print("Te sales por la derecha arriba")
	else:
		foundRU = True
		for c in range(0,len(word)):
			print(str(i)+"-"+str(j+c))
			print(matrix[i-c][j+c]+"=="+word[c])
			if matrix[i-c][j+c] != word[c]:
				foundRU = False
				print("not equal")
		if foundRU:
			print("Encontrada derecha arriba")
			dups = dups + 1
	#To left
	print("UP LEFT")
	if(((j+1)-len(word)) < 0 or ((i+1)-len(word)) < 0):
		print("Te sales por la izquierda arriba")
	else:
		foundLU = True
		for c in range(0,len(word)):
			print(str(i-c)+"-"+str(j-c))
			print(matrix[i-c][j-c]+"=="+word[c])
			if matrix[i-c][j-c] != word[c]:
				foundLU = False
				print("not equal")
		if foundLU:
			print("Encontrada izquierda arriba")
			dups = dups + 1
	return dups
	
def diagonals_down(i,j,matrix,word):
	downs = 0
	#To right
	print("DOWN RIGHT")
	if((j+len(word)) > len(matrix[i]) or ((i+len(word)) > len(matrix))):
		print("Te sales por la abajo derecha")
	else:
		foundRD = True
		for c in range(0,len(word)):
			print(str(i)+"-"+str(j+c))
			print(matrix[i+c][j+c]+"=="+word[c])
			if matrix[i+c][j+c] != word[c]:
				foundRD = False
				print("not equal")
		if foundRD:
			print("Encontrada derecha abajo")
			downs = downs + 1
	#To left
	print("DOWN LEFT")
	

	if(((j+1)-len(word)) < 0 or ((i+len(word)) > len(matrix))):
		print("Te sales por la abajo izquierda")
	else:
		foundLD = True
		for c in range(0,len(word)):
			print(str(i-c)+"-"+str(j+c))
			print(matrix[i+c][j-c]+"=="+word[c])
			if matrix[i+c][j-c] != word[c]:
				foundLD = False
				print("not equal")
		if foundLD:
			print("Encontrada izquierda abajo")
			downs = downs + 1
	return downs
	


array = []
word = "XMAS"

datafile = open('input4', 'r')

for row in datafile:
	l = list(row)
	l = l[:-1]
	array.append(l)

print_array(array)


founds = 0
for i in range(0,len(array)):
	print("Fila "+str(array[i]))
	for j in range(0,len(array[i])):
		print(array[i][j])
		if (array[i][j] == word[0]):
			print("buscando "+str(i)+"-"+str(j))
			
			founds = founds + horizontals(i,j,array,word)
			founds = founds + verticals(i,j,array,word)
			founds = founds + diagonals_up(i,j,array,word)
			founds = founds + diagonals_down(i,j,array,word)
	print()
print(founds)
	

