

datafile = open('input5', 'r')

rules = dict()

total = 0

def is_correct(before,later,rules):
	accepted = True
	if later in rules.keys():
		#print(str(updates[i])+"está en rules.keys() "+str(rules.keys()))
		if before in rules[later]:
			#print(str(updates[i]) + " tiene que ser posterior a "+str(updates[j]))
			accepted = False
	return accepted

incorrects = []

for row in datafile:
	if row.find("|") != -1:
		x,y = row.split("|")
		x=int(x)
		y=int(y)
		if x in rules:
			rules[x].append(y)
		else:
			rules[x]=list()
			rules[x].append(y)
	print(str(rules))

	if row.find(",") != -1:
		updates = [int(x) for x in row.split(",")]
		accepted = True
		for i in range(0,len(updates)):
			for j in range(i,len(updates)):
				print(updates[i])
				if not is_correct(updates[i],updates[j],rules):
					accepted = False
					
		if accepted:
			total = total + updates[int((len(updates) - 1)/2)]
		else:
			incorrects.append(updates)
print(total)

total2 = 0
print(len(incorrects))
for inc in incorrects:
	for i in range(0,len(inc)):
			for j in range(i,len(inc)):
				if not is_correct(inc[i],inc[j],rules):
					aux = inc[i]
					inc[i] = inc[j]
					inc[j] = aux
	
	total2 = total2 + inc[int((len(inc) - 1)/2)]
print(total2)

datafile.close()