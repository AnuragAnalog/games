
CC = gcc
CCC = $(CC) -c
FLAGS = -Wall
TARGET = rock_paper_scissors
DEBUG = -g

all:	rps
	$(CC) $(FLAGS) rps.o rpsmain.c -o $(TARGET) $(DEBUG)

clean:
	rm *.o $(TARGET)

rps:
	$(CCC) rps.c
