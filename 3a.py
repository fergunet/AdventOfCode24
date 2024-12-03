import re

datos = ""
with open('input3', 'r') as file:
	data = file.read()
	datos = data

p = re.compile('mul\([\d]{1,3},[\d]{1,3}\)|don\'t\(\)|do\(\)')
l = p.findall(data)
print(l)
result = 0
activate = True
for i in l:
	print(i)
	if(i == "do()"):
		activate=True
		print("DO")
		continue
	if(i == "don't()"):
		activate=False
		print("DONT")
	if(activate):
		p=re.compile('[\d]{1,3}')
		nums = p.findall(i)
		#print(nums)
		result = result + int(nums[0])*int(nums[1])
		print(result)
