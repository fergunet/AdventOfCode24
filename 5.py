

datafile = open('input5', 'r')

rules = dict()

total = 0

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
				if updates[j] in rules.keys():
						print(str(updates[i])+"está en rules.keys() "+str(rules.keys()))
						if updates[i] in rules[updates[j]]:
							print(str(updates[i]) + " tiene que ser posterior a "+str(updates[j]))
							accepted = False
		if accepted:
			total = total + updates[int((len(updates) - 1)/2)]
print(total)			



datafile.close()