/********* DEFINED CONSTANTS *********/
#define   MAX        32

/********* FUNCTION DECLARATION *********/
int menu();
int randno();
int lap_choice(int randnum);
int ur_choice(int score_lap, int score_ur);
int cal_score(int choice_lap, int choice_ur);
void game(int choice_lap, int choice_ur, int randnum);
void print_score(int score, int score_lap, int score_ur);
