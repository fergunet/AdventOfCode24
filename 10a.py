def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

def count_levels(i,j,level,array):
		
	#print(f" "+(level*" ")+f"{level}   {i},{j}, {level}")
	total = 0
	
	if i<0 or i>=len(array) or j<0 or j>=len(array[0]):
		return 0
	
	if array[i][j] == 9 and level==9:
		print("FOUND NEW")
		return 1
	
	if array[i][j] != level:
		return 0	
	else:
		print("[[")
		#total = total + count_levels(i-1,j-1,level+1,array)
		total = total + count_levels(i-1,j,level+1,array)#
		#total = total + count_levels(i-1,j+1,level+1,array)
		total = total + count_levels(i,j-1,level+1,array)#
		total = total + count_levels(i,j+1,level+1,array)#
		#total = total + count_levels(i+1,j-1,level+1,array)
		total = total + count_levels(i+1,j,level+1,array)#
		#total = total + count_levels(i+1,j+1,level+1,array)
		print("]]")
	return total


datafile = open('input10', 'r')

array=[]

for row in datafile:
	row = row.replace("\n","")
	l = list(row)
	l = [int(i) for i in l]
	array.append(l)

total = 0

print_array(array)

for i in range(0,len(array)):
	for j in range(0,len(array[i])):
		print(f"{i},{j},{array[i][j]}")
		if array[i][j] == 0:
			pathnums = count_levels(i,j,0,array)
			print(pathnums)
			total = total + pathnums
print(total)
