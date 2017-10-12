import re 

dataFile = open('actualdata.txt')
dataFile = dataFile.read()
numbers = re.findall('[0-9]+', dataFile)
# print(numbers)
lst = sum([int(num) for num in numbers])
print(lst)