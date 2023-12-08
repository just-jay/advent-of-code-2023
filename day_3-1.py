import re

def isSymbolAdjacent(i,j,lines):
    # 8 neighbors, we need to check each and check if its in bounds
	#1 2 3
	#4 X 5
	#6 7 8

	if i-1 > 0 and j-1 > 0 and lines[i-1][j-1] in SPECIAL: #1
		return True
	elif i-1 > 0 and lines[i-1][j] in SPECIAL: #2
		return True

	else:		
		return False

f = open("advent_file_3", "r")
lines = f.readlines()

SPECIAL = ["!","@","#","$","%","^","&","-","+","="]
NUMBER = ["1","2","3","4","5","6","7","8","9","0"]
sum = 0

# numList = [] # list of all numbers per line
# for i in range(0,len(lines)):
# 	numList.append(re.findall("[0-9]+",lines[i]))

f = -1 #front index
b = -1 #back index

for i in range(0,len(lines)):
	curr = ""
	for j in range(0, len(lines)):
		adj = False
		if lines[i][j] in NUMBER: #found first digit
			f = j
			curr += lines[i][j]
			# adj = isSymbolAdjacent(i,j,lines) || adj
		elif f != -1 and lines[i][j] not in NUMBER or : #if we've set the first digit and  
			b = j-1
			print(curr)
			# adj = isSymbolAdjacent(i,j-1,lines) || adj
			if adj: 
				sum += int(curr)
			adj = False
			curr = "" # reset local values
			f = -1 
			b = -1
		elif f != -1 and b == -1: # in middle of number
			curr += lines[i][j]
			# adj = isSymbolAdjacent(i,j,lines) || adj
		else: #found symbol - skip
			continue


print(sum)