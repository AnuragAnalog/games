import random
tries = 0
words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']
print("Welcome to jumbled words game:")
word = random.choice(words)
random_word = random.sample(word, len(word))
jumbled = ''.join(random_word)
print(f'Here is your word: {jumbled}')
s = input("Enter the correct answer:")
tries+=1
while s!= word:
  tries+=1
  s = input("Incorrect.\n Try again\n")
  
  if s==word:
    break

print("Correct!")
print("You took", tries, "tries" )

exit()

