board =  [[1,6,8] , [7,"X","X"] ,["X",5,"X"] ,
		 ["X",2,"X"] ,["X","X","X"] ,[6,"X",4] ,
		 ["X","X",3] ,["X","X",1] ,["X","X","X"] ,
		 ["X","X","X"] ,[4,2,"X"] ,["X","X","X"] ,
		 ["X","X","X"] ,[3,5,"X"] ,["X","X","X"] ,
		 ["X","X",7] ,["X","X",6] ,["X","X","X"] ,
		 ["X",8,"X"] ,["X","X","X"] ,[7,"X","X"] ,
		 [9,"X","X"] ,["X","X","X"] ,["X",8,"X"] ,
		 ["X","X","X"] ,["X","X","X"] ,["X","X",9]]
def print_board(board):
	for i in range(len(board)):
		if i not in [0,3,6,9,12,15,18,21,24]:	
			print(" " , "|" , end="")
		if i in [3,6,9,12,15,18,21,24]:
			print("")
			# print("")
		for j in range(3):
			print(" " , board[i][j] , end = "")
		if i in [8,17]:
			print("\n","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
def find_x(board):
	for i in range(27):
		for j in range(3):
			if board[i][j] == "X":
				return (i,j)
	return None	
def pos_check(bo,num,pos):
#row
	a,b = pos
	c = a%3
	a -= c
	for i in range(3):
		for j in range(3):
			if bo[a][j] == num:
				return False
		a += 1
#column
	a,b = pos
	if a in [3,6,9,12,15,18,21,24]:
		a = 0
	elif a in [4,7,10,13,16,19,22,25]:
		a = 1
	elif a in [5,8,11,14,17,20,23,26]:
		a = 2
	for i in range(9):
		if bo[a][b] == num:	
			return False
		a+=3
#block
	a,b = pos
	c = a%3
	if a>= 0 and a<=8:
		for i in range(3):
			for j in range(3):
				if bo[c][j] == num:
					return False
			c += 3
	elif a >= 9 and a<=	17:
		if c in [0,1,2]:
			a = 9 + c
			for i in range(3):
				for j in range(3):
					if bo[a][j] == num:
						return False
				a += 3
	elif a >= 18 and a <= 26:
		if c in [0,1,2]:
			a = 18 + c
			for i in range(3):
				for j in range(3):
					if bo[a][j] == num:
						return False
				a += 3
	return True
def solve(bo):
	find = find_x(bo)
	if not find:
		return True
	else:
		row, col = find
	for i in range(1,10):
		if pos_check(bo, i, (row, col)):
			bo[row][col] = i
			if solve(bo):
				return True
		bo[row][col] = "X"
	return False

print_board(board)
solve(board)
print("\n"*2)
print("boo yaaaaaaaaa!!!!!!!!!!!!!!!!!!!!!!" , "\n"*2)
print_board(board)
# print(pos_check(board,,(19,2)))