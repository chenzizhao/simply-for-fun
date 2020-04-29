/** snake API for C **/
// need to add the elongating of snek after nomming
#include "snek_api.h"
#include <string.h>
#include <time.h>

int TIME_OUT = ((BOARD_SIZE * 4) - 4) * CYCLE_ALLOWANCE;

GameBoard* init_board(){
	struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);

    /* using nano-seconds instead of seconds */
    srand((time_t)ts.tv_nsec);
	// srand(time(0));

	GameBoard* gameBoard = (GameBoard*)(malloc(sizeof(GameBoard)));

	for (int i = 0; i < BOARD_SIZE; i++){
		for (int j = 0; j < BOARD_SIZE; j++){
			gameBoard->cell_value[i][j] = 0;
			gameBoard->occupancy[i][j] = 0;
		}
	}
	gameBoard->occupancy[0][0] = 1; //snake initialized
	gameBoard->snek = init_snek(0, 0);
	gameBoard->CURR_FRAME=0;
	gameBoard->SCORE=0;
	gameBoard->MOOGLES_EATEN=0;
	gameBoard->MOOGLE_FLAG=0;
	return gameBoard;
}

Snek* init_snek(int a, int b){
	Snek* snek = (Snek *)(malloc(sizeof(Snek)));

	snek->head = (SnekBlock *)malloc(sizeof(SnekBlock));
	snek->head->coord[x] = a;
	snek->head->coord[y] = b;

	snek->tail = (SnekBlock *)malloc(sizeof(SnekBlock));
	snek->tail->coord[x] = a;
	snek->tail->coord[y] = b;

	snek->tail->next = NULL;
	snek->head->next = snek->tail;
	
	snek->length = 1;

	return snek;
}
//updated
int hits_edge(int axis, int direction, GameBoard* gameBoard){
	if (((axis == AXIS_Y) && ((direction == UP && gameBoard->snek->head->coord[y] + UP < 0) || (direction == DOWN && gameBoard->snek->head->coord[y] + DOWN > BOARD_SIZE - 1)))
	   || (axis == AXIS_X && ((direction == LEFT && gameBoard->snek->head->coord[x] + LEFT < 0) || (direction == RIGHT && gameBoard->snek->head->coord[x] + RIGHT > BOARD_SIZE-1))))
	{
		return 1;
	} else {
		return 0;
	}

}

//updated
int hits_self(int axis, int direction, GameBoard *gameBoard){
	int new_x, new_y;
	if (axis == AXIS_X){
		new_x = gameBoard->snek->head->coord[x] + direction;
		new_y = gameBoard->snek->head->coord[y];
	} else if (axis == AXIS_Y){
		new_x = gameBoard->snek->head->coord[x];
		new_y = gameBoard->snek->head->coord[y] + direction;
	}
	if ((gameBoard->snek->length != 1) && 
		(new_y == gameBoard->snek->tail->coord[y] && new_x == gameBoard->snek->tail->coord[x]))
	{
		return 0; //not hit self, this is the tail which will shortly be moving out of the way
	} else {
		return gameBoard->occupancy[new_y][new_x]; //1 if occupied
	}
}

int time_out(GameBoard *gameBoard){
	return (gameBoard->MOOGLE_FLAG == 1 && gameBoard->CURR_FRAME > TIME_OUT);

}

int is_failure_state(int axis, int direction, GameBoard *gameBoard){
	return (hits_self(axis, direction, gameBoard) || hits_edge(axis, direction, gameBoard) || time_out(gameBoard));
}

void populate_moogles(GameBoard *gameBoard){
	if (gameBoard->MOOGLE_FLAG == 0){
		int r1 = rand() % BOARD_SIZE;
		int r2 = rand() % BOARD_SIZE;
		
		int r3 = rand() % (BOARD_SIZE * 10);
		if (r3 == 0){
			gameBoard->cell_value[r1][r2] = MOOGLE_POINT * HARRY_MULTIPLIER;
			gameBoard->MOOGLE_FLAG = 1;
		} else if (r3 < BOARD_SIZE){
			gameBoard->cell_value[r1][r2] = MOOGLE_POINT;
			gameBoard->MOOGLE_FLAG = 1;
		}
	}
}

void eat_moogle(GameBoard* gameBoard, int head_x, int head_y) {
	gameBoard->SCORE = gameBoard->SCORE + gameBoard->cell_value[head_y][head_x];
	gameBoard->cell_value[head_y][head_x] = 0;

	gameBoard->snek->length ++;
	gameBoard->MOOGLES_EATEN ++;
	gameBoard->MOOGLE_FLAG = 0;
	gameBoard->CURR_FRAME = 0;
}

int advance_frame(int axis, int direction, GameBoard *gameBoard){
	// printf("DEBUG: in advance frame: nextAxis=%d, nextDir=%d\n", axis, direction);
	if (is_failure_state(axis, direction, gameBoard)){
		return 0;
	} else {
		// update the occupancy grid and the snake coordinates
		int head_x, head_y;
		// figure out where the head should now be
		if (axis == AXIS_X) {
			head_x = gameBoard->snek->head->coord[x] + direction;
			head_y = gameBoard->snek->head->coord[y];
		} else if (axis == AXIS_Y){
			head_x = gameBoard->snek->head->coord[x];
			head_y = gameBoard->snek->head->coord[y] + direction;
		}
		
		int tail_x = gameBoard->snek->tail->coord[x];
		int tail_y = gameBoard->snek->tail->coord[y];

		// printf("DEBUG: new head @ (%d, %d)\n", head_x, head_y);

		// update the occupancy grid for the head
		gameBoard->occupancy[head_y][head_x] = 1;

		if (gameBoard->snek->length > 1) { //make new head
			SnekBlock *newBlock = (SnekBlock *)malloc(sizeof(SnekBlock));
			newBlock->coord[x] = gameBoard->snek->head->coord[x];
			newBlock->coord[y] = gameBoard->snek->head->coord[y];
			newBlock->next = gameBoard->snek->head->next;
			gameBoard->snek->head->coord[x] = head_x;
			gameBoard->snek->head->coord[y] = head_y;
			gameBoard->snek->head->next = newBlock;

			if (gameBoard->cell_value[head_y][head_x] > 0){  //eat something
				eat_moogle(gameBoard, head_x, head_y);
			} else { //did not eat
				//delete the tail
				gameBoard->occupancy[tail_y][tail_x] = 0;
				SnekBlock *currBlock = gameBoard->snek->head;
				// added
				while (currBlock->next != gameBoard->snek->tail)
				// while(currBlock->next->coord[x]!=gameBoard->snek->tail->coord[x]
				// || currBlock->next->coord[y]!=gameBoard->snek->tail->coord[y])
				{
					// printf("DEBUG: currBlock @ (%d, %d)\n", currBlock->coord[x], currBlock->coord[y]);
					currBlock = currBlock->next;
					// printf("DEBUG: updated currBlock @ (%d, %d)\n", currBlock->coord[x], currBlock->coord[y]);
					// printf("DEBUG: here is what will be compared next:\n");
					// printf("%p VS %p\n", currBlock->next, gameBoard->snek->tail);
				} //currBlock->next points to tail
				currBlock->next = NULL;
				free(gameBoard->snek->tail);
				gameBoard->snek->tail = currBlock;
			}

		} else if ((gameBoard->snek->length == 1) && gameBoard->cell_value[head_y][head_x] == 0){ // change both head and tail coords, head is tail
			gameBoard->occupancy[tail_y][tail_x] = 0;
			gameBoard->snek->head->coord[x] = head_x;
			gameBoard->snek->head->coord[y] = head_y;
			gameBoard->snek->tail->coord[x] = head_x;
			gameBoard->snek->tail->coord[y] = head_y;
			
		} else { //snake is length 1 and eats something
			eat_moogle(gameBoard, head_x, head_y);
			gameBoard->snek->head->coord[x] = head_x;
			gameBoard->snek->head->coord[y] = head_y;
		}

		// update the score and board
		gameBoard->SCORE = gameBoard->SCORE + LIFE_SCORE;
		if (gameBoard->MOOGLE_FLAG == 1){
			gameBoard->CURR_FRAME ++;
		}

		// populate moogles
		populate_moogles(gameBoard);
		return 1;
	} 
}

void show_board(GameBoard* gameBoard) {
	fprintf(stdout, "\033[2J"); // clear terminal ANSI code
	fprintf(stdout, "\033[0;0H"); // reset cursor position
	
	char blank = 	43;
	char snek = 	83;
	char moogle = 	88;

	for (int i = 0; i < BOARD_SIZE; i++){
		for (int j = 0; j < BOARD_SIZE; j++){
			if (gameBoard->occupancy[i][j] == 1){
				//snake is here
				fprintf(stdout, "%c", snek);
			} else if (gameBoard->cell_value[i][j] > 0) {
				//there be a moogle
				fprintf(stdout, "%c", moogle);
			} else {
				//nothing to see here
				fprintf(stdout, "%c", blank);
			}
		} //new line
		fprintf(stdout, "\n");
		
	}

	fprintf(stdout, "\n\n");
	
	if (gameBoard->MOOGLE_FLAG == 1){
		fprintf(stdout, "!..ALERT, MOOGLE IN VICINITY..!\n\n");
	}
	fprintf(stdout, "SCORE: %d\n", gameBoard->SCORE);
	fprintf(stdout, "YOU HAVE EATEN %d MOOGLES\n\n", gameBoard->MOOGLES_EATEN);

	fprintf(stdout, "SNEK HEAD\t(%d, %d)\n", gameBoard->snek->head->coord[x], gameBoard->snek->head->coord[y]);
	fprintf(stdout, "SNEK TAIL\t(%d, %d)\n", gameBoard->snek->tail->coord[x], gameBoard->snek->tail->coord[y]);
	fprintf(stdout, "LENGTH \t%d\n", gameBoard->snek->length);
	fprintf(stdout, "CURR FRAME %d vs TIME OUT %d\n", gameBoard->CURR_FRAME, TIME_OUT);


	fflush(stdout);
}

int get_score(GameBoard *gameBoard) {
	return gameBoard->SCORE;
}

// GameBoard* _copy_board(GameBoard* board){
// 	GameBoard* newBoard = (GameBoard*)(malloc(sizeof(GameBoard)));
// 	for (int i = 0; i < BOARD_SIZE; i++){
// 		for (int j = 0; j < BOARD_SIZE; j++){
// 			newBoard->cell_value[i][j] = board->cell_value[i][j];
// 			newBoard->occupancy[i][j] = board->occupancy[i][j];
// 		}
// 	}
// 	// TODO copy snek
// 	Snek* snek=board->snek;
// 	SnekBlock* curr=snek->head;
// 	Snek* newSnek = (Snek *)(malloc(sizeof(Snek)));
// 	newSnek->head = (SnekBlock *)malloc(sizeof(SnekBlock));
// 	SnekBlock* currNew=newSnek->head;
// 	// DEBUG
// 	while(curr && curr->next){
// 		currNew->coord[x]=curr->coord[y];
// 		currNew->coord[y]=curr->coord[y];
// 		currNew->next=(SnekBlock *)malloc(sizeof(SnekBlock));
// 		currNew=currNew->next;
// 		curr=curr->next;
// 	}
// 	newSnek->tail=curr;
// 	newSnek->tail->next=NULL;
// 	newSnek->length = snek->length;
// 	newBoard->snek = newSnek;
// 	return newBoard;
// }

void _del_board(GameBoard **board){
	// need to free all allocated memory
	// first snek
	SnekBlock **snekHead = &((*board)->snek->head);
	SnekBlock *curr;
	SnekBlock *prev;
	while ((*snekHead)->next != NULL) {
		curr = *snekHead;
		while (curr->next != NULL){
			prev = curr;
			curr = curr->next;
		}
		prev->next = NULL;
		free(curr);
	}
	free(*snekHead);
	free((*board)->snek);
	free(*board);
}

void end_game(GameBoard **board){
	//fprintf(stdout, "\033[2J");
	//fprintf(stdout, "\033[0;0H"); 
	fprintf(stdout, "\n\n\n--!!---GAME OVER---!!--\n\nYour score: %d\n\n\n\n", (*board)->SCORE);
	fflush(stdout);
	_del_board(board);
}
