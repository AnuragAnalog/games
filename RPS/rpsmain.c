#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "rps.h"

/********* MAIN STARTS HERE *********/
int main(void)
{
   int       randnum = 0, option;
   int       choice_lap = 0, choice_ur = 0; 

   option = menu();

   switch (option)
   {
      case 1:
             game(choice_lap, choice_ur, randnum);
      case 2:
             exit(0);
   }

   exit(0);
}

