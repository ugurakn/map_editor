# parses string of single digit numbers into np array based on desired num of cols and rows 
#str_to_array(numStr, (row, column))

import numpy as np

def str_to_array(numStr, shape): 
	
	# parse row, col out of str shape
	shape = shape.strip("\n")
	index = shape.find(",") 
	row = int(shape[0:index])
	col = int(shape[index+1:])
	#print(f"{row=}, {col=}")

	assert row * col == len(numStr), "row x column does not match the given string of digits"

	strLst= []

	for i in range(len(numStr) // col):
		slice_index = i * col
		sliced_num  = numStr[slice_index : slice_index + col]
		#print(sliced_num)
		strLst.append(sliced_num)

	dgtLst = []
	for i, num in enumerate(strLst):
		dgtLst.append([])
		for digit in num:
			dgtLst[i].append(digit)
	
	# turn str to int
	intLst = [[int(digit) for digit in i] for i in dgtLst] # nested list comprehension

	# create array with the list
	arr = np.array(intLst, dtype="int8")

	return arr


if __name__ == "__main__":
	with open("maps.txt") as file:
		text = file.readlines()

		shape = text[0]
		mapStr = text[1]
		
	arr = str_to_array(mapStr, shape)

	print(arr)


