def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

def count_levels(i,j,level,array, origin, paths_finished):
		
	#print(f" "+(level*" ")+f"{level}   {i},{j}, {level}")
	total = 0
	
	if i<0 or i>=len(array) or j<0 or j>=len(array[0]):
		return 0
	
	if array[i][j] == 9 and level==9:
		current_path = f"{origin}{i}{j}"
		print(current_path)
		if current_path in paths_finished:
			print("Exists")
		else:
			paths_finished.append(current_path)
			print("FOUND NEW")
		return 1
	
	if array[i][j] != level:
		return 0	
	else:
		print("[[")
		#total = total + count_levels(i-1,j-1,level+1,array)
		total = total + count_levels(i-1,j,level+1,array,origin, paths_finished)#
		#total = total + count_levels(i-1,j+1,level+1,array)
		total = total + count_levels(i,j-1,level+1,array,origin, paths_finished)#
		total = total + count_levels(i,j+1,level+1,array,origin, paths_finished)#
		#total = total + count_levels(i+1,j-1,level+1,array)
		total = total + count_levels(i+1,j,level+1,array,origin, paths_finished)#
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
			paths=[]
			origin = f"[{i},{j}]"
			pathnums = count_levels(i,j,0,array,origin, paths)
			print(pathnums)
			total = total + len(paths)
print(total)
print(len(paths))