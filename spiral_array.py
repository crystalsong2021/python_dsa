def spiralTraverse(array):

    result = []
	startRow, endRow = 0, len(array)
	startCol, endCol = 0, len(array[0])

	while startRow < endRow and startCol < endCol:
		#traverse to right
		for col in range(startCol, endCol):
			result.append(array[startRow][col])

		#traverse downwards
		for row in range(startRow + 1, endRow):
			result.append(array[row][endCol - 1])

		#traverse backward
		for col in reversed(range(startCol, endCol - 1)):
			if startRow + 1 == endRow:
				break
			result.append(array[endRow-1][col])

		#traverse upward
		for row in reversed(range(startRow + 1, endRow - 1)):
			if startCol + 1 == endCol:
				break
			result.append(array[row][startCol])

		startRow += 1
		endRow -= 1
		startCol += 1
		endCol -= 1

	print('Final Result-->', result)
	return result


