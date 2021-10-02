import random

words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']
print("Welcome to jumbled words game:")
word = random.choice(words)
random_word = random.sample(word, len(word))
jumbled = ''.join(random_word)
print(f'Here is your word: {jumbled}')
s = input("Enter the correct answer:")
if s == word:
	print("Correct")
else:
	print("Try again next time!!")
