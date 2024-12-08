def print_array(array):
	for i in array:
		for j in i:
			print(j, end=" ")
		print()
	print()

def collinear(x1,  y1,  x2,  y2,  x3,  y3):
	if x1 == x2 and y1 == y2:
		return False
	if x1 == x3 and y1 == y3:
		return False
	if x2 == x3 and y2 == y3:
		return False
	return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2);




def is_hotspot(i,j, array):
	#print(f"Is hotspot {i} {j}")
	if array[i][j] != ".":
		return True
	rows = len(array)
	columns = len(array[0])
	for c in range(0,rows):
		for d in range(0,columns):
			for e in range(0,rows):
				for f in range(0,columns):
					#print(f"{c},{d} {e},{f}")
					if array[c][d] == array[e][f] and array[c][d] != ".":
						#print(f"{array[c][d]} == {array[e][f]} ")					
						if collinear(i,j,c,d,e,f):
							print("Colinear")
							print(f"{i},{j} {c},{d} {e},{f}")
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