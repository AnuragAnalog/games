# UCL LegendsGame
import turtle
from turtle import Screen
import winsound
import time
#Intro, Team and scores info:
print('Welcome to UCL Champions! Test your trial against the greatest clubs in Champions league History!')
print('Use W and S keys for moving left paddle up and down. Use Up and Down arrows to move the right paddle')
print('Right paddle can be moved in 2 player game!')
print('Select your Club!')
print('Enter integer corresponding to the club you want to play for')
print(' 1.  Manchester United\n 2.  Juventus Turin\n 3.  Bayern Munich\n 4.  Manchester City\n 5.  Borussia Dortmund\n 6.  Paris St.Germain' )
team = {1:  'Manchester United' , 2:'Juventus' ,3: 'Bayern Munich' ,4:'Manchester City',5:'Borussia Dortmund', 6:'Paris St. Germain'}
#Setting the Ballon d'or nominees:
ballondor= {1: ['Cristiano Ronaldo', 93], 2:['Federico Chiesa', 85], 3:['Robert Lewandowski', 91], 4:['Kevin De Bruyne', 91], 5:['Erling Haaland', 89], 6:['Lionel Messi.', 94], 7:['Zlatan Ibrahimovic', 87], 8:['Ansu Fati', 83],9:['Karim Benzema', 91] }

club = int(input())
if(club> 6 or club < 0):
    print('Please re read instructions and try again next time. Adios!')
    exit()
else:
    print('So, your club of choice is '  + team[club])
print('Do you want a two-player game(Press 1) or VS computer (Press 0)')
player = int(input())
if(player> 1 or player < 0):
    print('Please re read instructions and try again next time. Adios!')
    exit()
opp = {1: 'A.C Milan' , 2:'Barcelona' ,3: 'Real Madrid'}
AI = 0
if player == 0:
    AI = 1
    print('Select the champions you want to face off with')
    print(' 1. A.C Milan (Easy) \n 2. Barcelona (Medium)\n 3. Real Madrid (Hard)')
else:
    AI = 0
    print('Select team for Player 2:')
    print(' 1. A.C Milan \n 2. Barcelona \n 3. Real Madrid ')


oppo = int(input())
#Setting the craziness of REAL MADRID!!!
crazy = 0
if( oppo == 3):
    crazy =1
print('GET READY! Historic CHAMPIONS LEAGUE FINAL awaits! ')
print('Your Club is  ' + team[club])
print('Player Details: \n'  + 'Name: ' + ballondor[club][0] + ', Rating: ' +  str(ballondor[club][1]))
print('Opponent Club is '+ opp[oppo])
print('Player Details: \n'  + 'Name: ' + ballondor[6+oppo][0] + ', Rating: ' +  str(ballondor[6+oppo][1]))

print('Loading! ' + team[club] + ' VS ' + opp[oppo] + ' !')
print('                 '+str(ballondor[club][1])+ ' VS ' + str(ballondor[6+oppo][1]) )
print('Press Enter Key to START')
enter = input()



teamA = team[club]
teamB = opp[oppo]
scoreA = 0
scoreB = 0
if(oppo == 1 and AI == 1):
    win = 5
if(oppo == 2 and AI == 1):
    win = 2
elif(oppo == 3 and AI == 1):
    win = 3
else:
    win = 4
turn=1 #variable for speed

#Creating the window object
wn = turtle.Screen()   
wn .title('UCL Legends')
wn.bgcolor('darkgreen')
wn.setup(width = 800, height = 600)
wn.tracer(0)
#Field Boundary
l = turtle.Turtle()

l.hideturtle()
l.speed(0)
l.color("white")
l.pensize(10)

#Create field markers
l.left(90)
l.forward(270)
l.left(90)
l.forward(500)
l.left(90)
l.forward(540)
l.left(90)
l.forward(990)
l.left(90)
l.forward(540)
l.left(90)
l.forward(490)
l.left(90)
l.forward(540)

#Create Goal Posts
l.setpos(0,0)
l.right(90)
l.penup()
l.forward(400)
l.penup()
l.forward(100)
l.pendown()
l.right(90)
l.forward(135)
l.right(90)
l.forward(100)
l.right(90)
l.forward(270)
l.right(90)
l.forward(100)
l.penup()
l.goto(0,0)
l.pendown()
l.right(180)
l.penup()
l.forward(390)
l.penup()
l.forward(100)
l.pendown()
l.left(90)
l.forward(135)
l.left(90)
l.forward(100)
l.left(90)
l.forward(270)
l.left(90)
l.forward(100)





#Using Turtle Graphics to draw game objects
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #Sets the speed of animation to max possible speed
paddle_a.shape('square')
if club == 1:
    paddle_a.color('red')
elif club == 2:
    paddle_a.color('black')
elif club == 3:
    paddle_a.color('orange')
elif club == 4:
    paddle_a.color('lightblue')
elif club == 5:
    paddle_a.color('yellow')
else:
    paddle_a.color('darkblue')
paddle_a.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0) #Setting the positional coordinates


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #Sets the speed of animation to max possible speed
paddle_b.shape('square')
if oppo == 1:
    paddle_b.color('darkred')
elif oppo == 2:
    paddle_b.color('blue')
else:
    paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 4, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0) #Setting the positional coordinates


#Draw Midfield circle
# start circle

cir = turtle.Turtle()
cir.hideturtle()
cir.right(90)
cir.penup()
cir.forward(54)
cir.pendown()
cir.left(90)
cir.pensize(10)
cir.color('white')
cir.circle(40)


#Ball
ball= turtle.Turtle()
ball.speed(0) #Sets the speed of animation to max possible speed
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0) #Setting the positional coordinates
#Every time our ball moves it moves by 0.1 pixels
if (AI == 0):
    ball.dx = 0.6
    ball.dy = 0.6
else:
    ball.dx  = 0.6
    ball.dy = 0.6
#BALL 2
ball2= turtle.Turtle()
ball2.speed(0) #Sets the speed of animation to max possible speed
ball2.shape('circle')
ball2.color('black')
ball2.penup()
ball2.goto(0, -10) #Setting the positional coordinates
#Every time our ball moves it moves by 0..1 pixels
ball2.dx  = -0.6
ball2.dy = -0.6

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 290)
pen.write(teamA +  "  "+ str(scoreA)+"  "+ teamB + "  "+ str(scoreB), align = "center",  font = ("Bahnschrift" , 24, "normal"))


pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('orange')
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -310)

#Movement functions
def paddle_a_up():
    #Get current co-ordinate
    y = paddle_a.ycor()  #ycor is from the turtle module
    #Y increases as we go up and decreases when we go down
    if( AI ==1 and ballondor[club][1] > 91):
        y+= 26
    elif  AI ==1 and ballondor[club][1] > 90:
        y+= 24
    elif  AI ==1 and ballondor[club][1] > 85:
        y += 22
    else:
        y += 20
    paddle_a.sety(y) #Turtle module
def paddle_a_down  ():
    y = paddle_a.ycor()  #ycor is from the turtle module
    #Y increases as we go up and decreases when we go down
    if( AI ==1 and  ballondor[club][1] > 91):
        y-= 26
    elif ( AI ==1 and ballondor[club][1] > 90):
        y-= 24
    elif  (AI ==1 and ballondor[club][1] > 85):
        y -= 22
    else:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    #Get current co-ordinate
    y = paddle_b.ycor()  #ycor is from the turtle module
    #Y increases as we go up and decreases when we go down
    if(AI == 1):
         if (oppo == 1):
            y += 0.530
         elif oppo == 2:
            y +=  0.540
         elif oppo == 3:
             y += 0.550
    else:
         y+= 20
    paddle_b.sety(y) #Turtle module
def paddle_b_down  ():
    #Get current co-ordinate
    y = paddle_b.ycor()  #ycor is from the turtle module
    #Y increases as we go up and decreases when we go down
    if(AI == 1):
         if (oppo == 1):
            y += 0.530
         elif oppo == 2:
            y +=  0.540
         elif oppo == 3:
             y += 0.550
    else:
        y-= 20
    
    paddle_b.sety(y) #Turtle module


# Keyboard binding
wn.listen() #Listen for keyboard input
wn.onkeypress(paddle_a_up,  "w")
wn.onkeypress(paddle_a_down,"s" )
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




def byeTurtle():
    turtle.clear()
    return

#Main Game Loop
while True:
    wn.update()

    
    
    #Move the ball
    if(AI == 0):
        x_speed = 0.5*turn*ball.dx
        y_speed = 0.5*turn*ball.dy
    else:
        x_speed = ball.dx
        y_speed = ball.dy
    ball.setx(ball.xcor() + x_speed)
    ball.sety(ball.ycor() + y_speed)

    if(crazy == 1):
        ball2.setx(ball2.xcor() + ball2.dx)
        ball2.sety(ball2.ycor() + ball2.dy)

    #Paddle Check
    if paddle_a.ycor() > 238:
        paddle_a.sety(238)
    if paddle_a.ycor() < -238:
        paddle_a.sety(-238)

    if paddle_b.ycor() > 238:
        paddle_b.sety(238)
    if paddle_b.ycor() < -238:
        paddle_b.sety(-238)
    #Border Check
    if ball.ycor() >  250 :
        ball.sety(250)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.ycor() >134 and ball.ycor() <-134) and ball.xcor() >  460:
        ball.setx(460)
        ball.dy *= -1
        
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() <  -250 :
        ball.sety(-250)
        ball.dy *= -1 # Reverse ball directoion, akin to bouncing off
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ((ball.ycor() >134 and ball.ycor() <-134) and ball.xcor() <  -440):
        ball.setx(-460)
        ball.dy *= -1
        
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() > 420 and (ball.ycor() < 134 and ball.ycor() > -134))  :
        winsound.PlaySound("applause.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        
        scoreA += 1
        
        pen.clear()
        pen.write(teamA + "  "+ str(scoreA) +"  "+ teamB+ "  "+ str(scoreB), align = "center",  font = ("Bahnschrift" , 24, "normal"))
        if scoreA >= win:
            pen.clear()
            pen.write(teamA+ ' ARE UEFA CL CHAMPIONS! (bt '+ teamB+ '  '+str(scoreA) + '-'+ str(scoreB) + ' )' , align = 'center' , font = ('arial' , 26 ,'normal'))
            pen2.write("BALLON D' OR winner:  " + ballondor[club][0]+  " !", align = "center",  font = ("Bahnschrift" , 24, "normal"))
            winsound.PlaySound("applause4.wav", winsound.SND_ASYNC)
            time.sleep(7)
            byeTurtle()
            break
   
    if ball2.ycor() >  250 :
            ball2.sety(250)
            ball2.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if  ball2.xcor() > 440 and (ball2.ycor() >134 and ball2.ycor() <-134) :
            ball2.setx(460)
            ball2.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball2.ycor() <  -250 :
            ball2.sety(-250)
            ball2.dy *= -1 # Reverse ball directoion, akin to bouncing off
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if  ball2.xcor() <  -440 and (ball2.ycor() >134 and ball2.ycor() <-134) :
            ball2.setx(-460)
            ball2.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball2.xcor() > 420 and (ball2.ycor() < 134 and ball2.ycor() > -134):
            winsound.PlaySound("applause.wav", winsound.SND_ASYNC)
            ball2.goto(0, 0)
            ball2.dx *= -1
            scoreA += 1
            pen.clear()
            pen.write(teamA + "  "+ str(scoreA) +"  "+ teamB+ "  "+ str(scoreB), align = "center",  font = ("Bahnschrift" , 24, "normal"))
            if scoreA >= win:
                pen.clear()
                pen.write(teamA+ ' ARE UEFA CL CHAMPIONS! (bt '+ teamB+ '  '+str(scoreA) + '-'+ str(scoreB) + ' )' , align = 'center' , font = ('arial' , 26 ,'normal'))
                pen2.write("BALLON D' OR winner:  " + ballondor[club][0] +  " !",align = "center",  font = ("Bahnschrift" , 24, "normal"))
                winsound.PlaySound("applause4.wav", winsound.SND_ASYNC)
                time.sleep(7)
                byeTurtle()
                break
                
     
    if ball.xcor() < -420 and (ball.ycor() < 134 and ball.ycor() > -134):
        winsound.PlaySound("applause.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(teamA +"  " +str(scoreA)+ "  " + teamB +"  "+ str(scoreB), align = "center",  font = ("Bahnschrift" , 24, "normal"))
        if scoreB >= win:
            pen.clear()
            pen.write(teamB+ ' are UEFA CL CHAMPIONS! (bt '+ teamA+ '  '+str(scoreB) + '-'+ str(scoreA) + ' )' , align = 'center' , font = ('arial' , 26 ,'normal'))
            pen2.write("BALLON D' OR winner:  " + ballondor[6+oppo][0] +  " !",align = "center",  font = ("Bahnschrift" , 24, "normal"))
            winsound.PlaySound("applause4.wav", winsound.SND_ASYNC)
            time.sleep(7)
            byeTurtle()
            break


        
    if ball2.xcor() < -420 and (ball2.ycor() < 134 and ball2.ycor() > -134):
                winsound.PlaySound("applause.wav", winsound.SND_ASYNC)
                ball2.goto(0, 0)
                ball2.dx *= -1
                scoreB += 1
                pen.clear()
                pen.write(teamA +"  " +str(scoreA)+ "  " + teamB +"  "+ str(scoreB), align = "center",  font = ("Bahnschrift" , 24, "normal"))
                if scoreB >= win:
                    pen.clear()
                    pen.write(teamB+ ' are UEFA CL CHAMPIONS! (bt '+ teamA+ '  '+str(scoreB) + '-'+ str(scoreA) + ' )' , align = 'center' , font = ('arial' , 26 ,'normal'))
                    pen2.write("BALLON D' OR winner:  " + ballondor[6+oppo][0]+  " !",align = "center",  font = ("Bahnschrift" , 24, "normal"))
                    winsound.PlaySound("applause4.wav", winsound.SND_ASYNC)
                    time.sleep(7)
                    byeTurtle()
                    break
                

     #Paddle Check
        # PADDLE at 350, width = 20 so 10 at one side and length is 100 so 50 one side
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        turn += 1
        ball.dx *= -1
        ball.speed(1)
        turn += 1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        turn += 1
        ball.dx *= -1
        ball.speed(1)
        
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
    if (ball2.xcor() > 340 and ball2.xcor() < 350) and (ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() -40):
            ball2.setx(340)
            ball2.dx *= -1
            ball2.speed(1)
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball2.xcor() < -340 and ball2.xcor() > -350) and (ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() -40):
            ball2.setx(-340)
            ball2.dx *= -1
            ball2.speed(1)
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


      #AI Player
    if(crazy == 0 and AI == 1):
            if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_up()
            if paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10 :
                paddle_b_down()
    if(crazy == 1 and AI == 1):
        if ball.xcor() > ball2.xcor():
            if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_up()

            elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
                paddle_b_down()
        else:
            if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                paddle_b_up()

            elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
                paddle_b_down()
            
























        
        
        
    
































    
    
