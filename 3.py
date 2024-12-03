import re

datos = ""
with open('input3', 'r') as file:
	data = file.read()
	datos = data

p = re.compile('mul\([\d]{1,3},[\d]{1,3}\)')
l = p.findall(data)
print(l)
result = 0
for i in l:
	print(i)
	p=re.compile('[\d]{1,3}')
	nums = p.findall(i)
	print(nums)
	result = result + int(nums[0])*int(nums[1])
	print(result)
