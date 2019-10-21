#Rock paper scissors
import random
def roshambo():
  print "0 = rock"
  print "1 = paper"
  print "2 = sicssor"
  x = int(input())
  a = [0,1,2]
  x1 = random.choice(a)
  if (x == x1) :
    print "Tie"
  if (x == 0 and x1 == 1):
    print "System wins"
  if (x == 1 and x1 == 0):
    print "player wins"
  if (x == 1 and x1 == 2):
    print "System wins"
  if (x == 2 and x1 == 1):
    print "player wins"
  if (x == 0 and x1 == 2):
    print "player wins"
  if (x == 2 and x1 == 0):
    print "system wins" 
# Give keyboard interrupt to break
while(True):
  roshambo()
