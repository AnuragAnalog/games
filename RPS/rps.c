#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "rps.h"

/********* FUNCTION DEFINITION *********/
int menu()
{
   int       opt;

   printf("\t\t  ------------------------  \t\n");
   printf("\t\t| ROCK - PAPER - SCISSORS |\t\n");
   printf("\t\t  ------------------------  \t\n");
   printf("\n");
   printf("\t\t 1) Start the Game\n");
   printf("\t\t 2) Exit\n");

   printf("Your option please:- ");
   scanf("%d", &opt);

   if (opt > 2 && opt < 1)
   {
      printf("Select from the above options only\n");
      exit(1);
   }

   return opt;
}

int randno()
{
   int       num = time(NULL);

   num = num * 1103515245 + 12345;
   return (num/65536) % 3;
}

int lap_choice(int randnum)
{
   randnum = randno();

   if (randnum < 0)
   {
      randnum = (-1) * randnum;
   }

   if (randnum == 0)
   {
      printf("My choice was ROCK.\n");
   }
   else if (randnum == 1)
   {
      printf("My choice was PAPER.\n");
   }
   else if (randnum == 2)
   {
      printf("My choice was SCISSORS.\n");
   }

   return randnum;
}

int ur_choice(int score_lap, int score_ur)
{
   int         check = 0;
   char        choice[MAX];

   printf("Select your choice:- \n");
   printf("1:ROCK     2:PAPER     3:SCISSORS\t\n");
   scanf("%s", choice);

   if (*choice >= '1' && *choice <= '3' && strlen(choice) == 1)
   {
      return (int)(*choice - '0');
   }
   else
   {
      printf("Thank you for playing the game.\n");
      if (score_ur > score_lap)
      {
         printf("Your luck is greater than my luck.\n");
      }
      else if (score_ur == score_lap)
      {
         printf("It seems we both have same amount of luck.\n");
      }
      else if (score_lap > score_ur)
      {
         printf("My luck is greater than your luck.\n");
      }

      exit(1);
   }
}

int cal_score(int choice_lap, int choice_ur)
{
   int        ur = 0, lap = 0, num = 0;

   if (choice_lap == 0 && choice_ur == 1)
   {
      ur = ur + 1;
   }
   else if (choice_lap == 0 && choice_ur == 2)
   {
      lap = lap + 1;
   }
   else if (choice_lap == 1 && choice_ur == 0)
   {
      lap = lap + 1;
   }
   else if (choice_lap == 1 && choice_ur == 2)
   {
      ur = ur + 1;
   }
   else if (choice_lap == 2 && choice_ur == 1)
   {
      lap = lap + 1;
   }
   else if (choice_lap == 2 && choice_ur == 0)
   {
      ur = ur + 1;
   }

   if (ur != 0)
   {
      return num = (num | (1 << ur));
   }
   else if (lap != 0)
   {
      return num = (num | (1 << (lap+1)));
   }

   return num;
}

void game(int choice_lap, int choice_ur, int randnum)
{
   int        score, score_lap = 0, score_ur = 0;

   printf("When you are done with playing the game then type any character ");
   printf("otherthan 1, 2, 3 to terminate the game.\n");
   while(1)
   {
      choice_ur = ur_choice(score_lap, score_ur) - 1;
      choice_lap = lap_choice(randnum);
      score = cal_score(choice_lap, choice_ur);

      switch (score)
      {
         case 0:
               printf("Both the choices are same.\n");
               break;
         case 2:
               score_ur = score_ur + 1;
               break;
         case 4:
               score_lap = score_lap + 1;
               break;
      }
      printf("+-------------------------------+\n");
      printf("| Your score\t| My score\t|\n");
      printf("+-------------------------------+\n");
      printf("|\t%d\t|\t%d\t|\n", score_ur, score_lap);
      printf("+-------------------------------+\n");
   }

   return ;
}
