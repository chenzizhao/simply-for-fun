from snek import *
from time import sleep
from copy import deepcopy
import logging
from statistics import mean, median, stdev

# My Strategies
def strategy_0(currAxis, currDir, board):
	"""
	Manual strategy: player input
		w
	a	s	d
	"""	
	nextAxis, nextDir = currAxis, currDir
	validInput=False
	while(not validInput):
		cmd=input("Put in your command: ")
		validInput = (cmd=="w" or cmd=="s" or cmd=="a" or cmd=="d")
		if not validInput:
			print("Invalid input -- try again")
	if cmd=="w":
		nextAxis, nextDir = AXIS_Y, UP
	elif cmd=="s":
		nextAxis, nextDir = AXIS_Y, DOWN
	elif cmd=="a":
		nextAxis, nextDir = AXIS_X, LEFT
	elif cmd=="d":
		nextAxis, nextDir = AXIS_X, RIGHT
	return [(nextAxis, nextDir)]


def strategy_1(currAxis, currDir, board):
	"""
	Default strategy: do nothing and follows the edge
	"""
	#indexing at 0 dereferences the pointer
	x_coord = board[0].snek[0].head[0].coord[x]
	y_coord = board[0].snek[0].head[0].coord[y]
	go_x = (currAxis == AXIS_Y and currDir == 1 and y_coord == (BOARD_SIZE - 1)) or \
			(currAxis == AXIS_Y and currDir == -1 and y_coord == 0)
	go_y = (currAxis == AXIS_X and currDir == 1 and x_coord == (BOARD_SIZE - 1)) or \
			(currAxis == AXIS_X and currDir == -1 and x_coord == 0)
	if go_x:
		nextAxis = AXIS_X
		nextDir = RIGHT if x_coord < BOARD_SIZE // 2 else LEFT
	elif go_y:
		nextAxis = AXIS_Y
		nextDir = DOWN if y_coord < BOARD_SIZE // 2 else UP
	else:
		nextAxis=currAxis
		nextDir=currDir
	return [(nextAxis, nextDir)]


def strategy_2(currAxis, currDir, board):
	"""
	Traverse fixed size board (even size)
	"""
	x_coord = board[0].snek[0].head[0].coord[x]
	y_coord = board[0].snek[0].head[0].coord[y]
	nextAxis=currAxis
	nextDir=currDir
	if x_coord==1:
		if y_coord%2==1:
			nextAxis, nextDir = AXIS_Y, DOWN
		else:
			nextAxis, nextDir = AXIS_X, RIGHT
	if x_coord==BOARD_SIZE-1:
		if y_coord%2==1:
			nextAxis, nextDir = AXIS_X, LEFT
		else:
			nextAxis, nextDir = AXIS_Y, DOWN
	if y_coord==BOARD_SIZE-1:
		if x_coord==0:
			nextAxis, nextDir = AXIS_Y, UP
		else: 
			nextAxis, nextDir = AXIS_X, LEFT
	if x_coord==0:
		if y_coord==0:
			nextAxis, nextDir = AXIS_X, RIGHT
		else:
			nextAxis, nextDir = AXIS_Y, UP
	return [(nextAxis, nextDir)]


def _greedy(nextAxis, nextDir, board):
	greedy=0
	# find head coord
	head=board[0].snek[0].head[0]
	x_coord_head=head.coord[x]
	y_coord_head=head.coord[y]
	# find new head coord
	if nextAxis==AXIS_X:
		x_coord_head+=nextDir
	elif nextAxis==AXIS_Y:
		y_coord_head+=nextDir
	# find moogle coord
	cell_value=board[0].cell_value
	foundMoogle=False
	for i in range(0, BOARD_SIZE):
		for j in range(0, BOARD_SIZE):
			if cell_value[i][j] != 0:
				y_coord_m=i
				x_coord_m=j
				foundMoogle=True
				break
		if foundMoogle: break
	if not foundMoogle:
		return 0
	# calculate distance
	dist=abs(x_coord_head-x_coord_m)+abs(y_coord_head-y_coord_m)
	# shorter distance, greater heur, better choice
	greedy=-dist
	return greedy


def strategy_3(currAxis, currDir, board):
	"""
	Greedy: does not prevent hitting itself
	"""
	heur=_greedy
	# all possible movement
	moves = [(AXIS_X, LEFT), (AXIS_X, RIGHT), (AXIS_Y, UP), (AXIS_Y, DOWN)]
	# moves.remove((currAxis, -currDir))
	heuristics = [float("-inf")]*len(moves)
	for i in range(len(moves)):
		nextAxis, nextDir=moves[i]
		# test if they are valid
		if not is_failure_state(nextAxis, nextDir, board):
			heuristics[i]=heur(nextAxis, nextDir, board)
	return [moves[heuristics.index(max(heuristics))]]


def play(verbal=False, wait=False, strategy=strategy_0):
	#ptr to board
	board = init_board()
	play_on = 1
	if verbal: show_board(board)
	axis = AXIS_INIT
	direction = DIR_INIT
	
	while (play_on):
		# Get instructions
		instructions = strategy(axis, direction, board)
		# Advance game
		while(instructions):
			axis, direction = instructions.pop(0)
			play_on = advance_frame(axis, direction, board)
			if verbal: show_board(board)
			if wait: sleep(0.05)
		
	#pass by reference to clean memory	
	score=get_score(board)
	end_game(byref(board))
	logging.info(f"{strategy.__name__} -> {score}")
	return score


if __name__ == "__main__":
	# CHANGE ME
	myStrategy=strategy_2
	mode=DEMO
	numTest=200
	logging.basicConfig(level=logging.INFO, filename="./py/main.log", format="%(asctime)s - %(levelname)s - %(message)s")

	if mode==DEMO:
		score=play(verbal=True, wait=True, strategy=myStrategy)
	
	elif mode==TEST:
		scores=[]
		for i in range(numTest):
			score=play(verbal=False, wait=False, strategy=myStrategy)
			scores.append(score)
		print(f"In TEST mode, the average score is {mean(scores)}+-{stdev(scores)}, with median of {median(scores)}. ")