import csv
import operator

#FILA[14, 11, 14, 17, 18, 19]
#FILA[65, 68, 71, 72, 71]

def differences_less_than(l, value):
	asciende = False
	if(l[0]<l[1]):
		asciende = True
	for i in range(0,len(l)-1):
		if(l[i]==l[i+1]):
			print("iguales")
			return False
		if(abs(l[i]-l[i+1])>value):
			print("diferencia")
			return False
		if(not((l[i]<l[i+1]) == asciende)):
			print("no sorted")
			return False
	return True

def check_all_levels(l):
	if(differences_less_than(l,3)):
		print("Seguro de primeras")
		return True
	else:
		print("Inseguro de primeras")
	for i in range(0,len(l)):
		copy = list(l)
		del copy[i]
		print(copy)
		if (differences_less_than(copy,3) == True):
			return True
	return False


reports = 0
with open('input2', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ')
	for row in spamreader:
		row = [int(c) for c in row]
		print("-----FILA"+str(row))
		if(check_all_levels(row)):
			reports = reports +1
			print("SSSSSSSSSSSSSSEGURO")
print(reports)




