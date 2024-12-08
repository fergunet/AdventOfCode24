def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

def another_in_double_position(id,i,j,orig_i,orig_j,array):

	
	if i == orig_i and j == orig_j:
		return False
	ni = i-(orig_i-i)
	nj = j-(orig_j-j)



	if ni < 0 or ni >= len(array):
		return False
	if nj < 0 or nj >= len(array[ni]):
		return False
	if array[ni][nj]==".":
		return False
	if id == array[ni][nj]:
		return True

	return False

def is_hotspot(i,j, array):
	print(f"Is hotspot {i} {j}")
	for c in range(0,len(array)):
		for d in range(0,len(array[i])):
			#print(f"Checking {array[i][j]} {c} {d} {i} {j}")
			if array[c][d] != ".":
				if(another_in_double_position(array[c][d],c,d,i,j,array)):
					return True

def count_hotspots(array):
	total = 0
	for i in range(0,len(array)):
		for j in range(0,len(array[i])):
			if(is_hotspot(i,j,array)):
				total = total+1
	return total


datafile = open('input8', 'r')

array=[]

for row in datafile:
	row = row.replace("\n","")
	l = list(row)
	array.append(l)

print_array(array)

print(count_hotspots(array))