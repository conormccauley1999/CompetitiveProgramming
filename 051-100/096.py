# Problem 96

def loadGrids():
	with open("../files/96.txt") as f:
		lns = f.readlines()
	lns = [x.strip() for x in lns] 
	ln = len(lns)
	grids = []
	for i in range(0, ln/10):
		grid = []
		for j in range(1, 10):
			lst = list(lns[(i*10)+j])
			g = [int(l) for l in lst]
			grid.append(g)
		grids.append(grid)
	return grids

def main():
	grids = loadGrids()
	sm = 0
	for i in range(0, len(grids)):
		grid = grids[i]
		sudoku(grid, 0, 0)
		v = (getSquare(grid, 0, 0) * 100) + (getSquare(grid, 0, 1) * 10) + (getSquare(grid, 0, 2))
		print v
		sm += v
	return sm

def sudoku(grid, row, column):
	
	result = False
	
	nextRow = row
	nextColumn = column + 1
	
	if nextColumn > 8:
		nextColumn = 0
		nextRow += 1
	
	if getSquare(grid, row, column) != 0:
		
		if row == 8 and column == 8:
			return True
		
		else:
			result = sudoku(grid, nextRow, nextColumn)
	
	else:
		
		attempt = 1
		
		while attempt <= 9 and not result:
			
			setSquare(grid, row, column, attempt)
			
			if isValid(grid, row, column):
				
				if row == 8 and column == 8:
					result = True
				
				else:
					result = sudoku(grid, nextRow, nextColumn)
			
			attempt += 1
		
		if not result:
			setSquare(grid, row, column, 0)
	
	return result

def isValid(grid, row, column):
	
	value = getSquare(grid, row, column)
	
	if value == 0:
		return True
	
	if rowValid(grid, row, column, value) and columnValid(grid, row, column, value) and subgridValid(grid, row, column, value):
		return True
	else:
		return False

def rowValid(grid, row, column, value):
	
	for i in range(0, 9):
		if i != row and value == getSquare(grid, i, column):
			return False
	
	return True

def columnValid(grid, row, column, value):
	
	for i in range(0, 9):
		if i != column and value == getSquare(grid, row, i):
			return False
	
	return True

def subgridValid(grid, row, column, value):
	
	startX = 3 * (row // 3)
	startY = 3 * (column // 3)
	
	offsetX = row % 3
	offsetY = column % 3
	
	for i in range(0, 3):
		for j in range(0, 3):
			
			if i != offsetX or j != offsetY:
				
				x = startX + i
				y = startY + j
				
				if getSquare(grid, x, y) == value:
					return False
	
	return True

def getSquare(grid, row, column):
	
	return grid[row][column]

def setSquare(grid, row, column, value):
	
	grid[row][column] = value

print main()
