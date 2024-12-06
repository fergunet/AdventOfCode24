from enum import Enum

class Dir(Enum):
	UP = "^"
	DOWN = "v"
	LEFT = "<"
	RIGHT = ">"
	END = "E"

def next_position(i,j,dir,array):
	rows = len(array)
	columns = len(array[i])

	if(dir == Dir.UP):
		if(i==0):
			return Dir.END,-1,-1
		if(array[i-1][j]=="#"):
			return Dir.RIGHT,i,j+1
		else:
			return Dir.UP,i-1,j
	
	if(dir == Dir.DOWN):
		if(i==(rows-1)):
			return Dir.END,-1,-1
		if(array[i+1][j]=="#"):
			return Dir.LEFT,i,j-1
		else: 
			return Dir.DOWN,i+1,j
	
	if(dir == Dir.RIGHT):
		if(j==(columns-1)):
			return Dir.END,-1,-1
		if(array[i][j+1]=="#"):
			return Dir.DOWN,i+1,j
		else:
			return Dir.RIGHT,i,j+1
	
	if(dir == Dir.LEFT):
		if(j==0):
			return Dir.END,-1,-1
		if(array[i][j-1]=="#"):
			return Dir.UP,i-1,j
		else:
			return Dir.LEFT,i,j-1



		

def current_position(array):
	for i in range(0,len(array)):
		for j in range(0,len(array[i])):
			#print(array[i][j])
			#print([item.value for item in Dir])
			if(array[i][j] in [item.value for item in Dir]):
				print("FOUND")
				return Dir(array[i][j]),i,j

def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

datafile = open('input6', 'r')

array=[]

for i,row in enumerate(datafile):
	row = row.strip()
	l = list(row)
	array.append(l)

print_array(array)

dir,ni,nj = current_position(array)
inside = True
array[ni][nj] = "X"

def count_values(array, value):
	total = 0
	for row in array:
		total = total + row.count(value)
	return total

while(inside):
	#print_array(array)
	dir,ni,nj = next_position(ni,nj,dir,array)
	
	if dir == Dir.END:
		break
	array[ni][nj] = "X"
	

print(count_values(array,"X"))
	
	