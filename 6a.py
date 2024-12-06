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
			return Dir.END,"-1","-1"
		if(array[i-1][j]=="#"):
			return Dir.RIGHT,i,j+1
		else:
			return Dir.UP,i-1,j
	
	if(dir == Dir.DOWN):
		if(i==(rows-1)):
			return Dir.END,"-1","-1"
		if(array[i+1][j]=="#"):
			return Dir.LEFT,i,j-1
		else: 
			return Dir.DOWN,i+1,j
	
	if(dir == Dir.RIGHT):
		if(j==(columns-1)):
			return Dir.END,"-1","-1"
		if(array[i][j+1]=="#"):
			return Dir.DOWN,i+1,j
		else:
			return Dir.RIGHT,i,j+1
	
	if(dir == Dir.LEFT):
		if(j==0):
			return Dir.END,"-1","-1"
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

def is_cicle(oni,onj,odir,array):
	ni = oni
	nj = onj
	dir = odir
	set_steps = set()
	while(True):
		#print_array(array)
		set_steps.add(str([dir,ni,nj]))
		if ni == -1:
			print ("HAY ERROR")
		dir,ni,nj = next_position(ni,nj,dir,array)
		if dir == Dir.END:
			return False
		if str([dir,ni,nj]) in set_steps:
			return True

datafile = open('input6', 'r')

array=[]

for row in datafile:
	row = row.strip()
	l = list(row)
	array.append(l)

print_array(array)

dir,ni,nj = current_position(array)

cicles = 0
for i in range(0,len(array)):
	print(i)
	for j in range(0,len(array[i])):
		if array[i][j] == ".":
			#print("Placing obstacle in "+str(i)+","+str(j))
			array[i][j] = '#'
			#print_array(array)
			if is_cicle(ni,nj,dir,array)==True:
				cicles = cicles + 1
			array[i][j] = "."
print(cicles)



	
	