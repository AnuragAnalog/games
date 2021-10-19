print('Welcome to the Python Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) : ')
score=0
total_questions=4
 
if answer.lower()=='yes':
    answer=input('Question 1: What is the capital of Australia? ')
    if answer.lower()=='canberra':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Have you got the vaccine? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Which is the smallest continent? ')
    if answer.lower()=='australia':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
    
     answer=input('Question 4: Which is the largest state in India? ')
    if answer.lower()=='rajasthan':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Thanks for playing !')

