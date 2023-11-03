import random
# from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives= 6

word_list=["camel","football","airplain"]

end_of_game= False

word_guess=[]

#Choose radom word for word_list
word=random.choice(word_list)
print(word)

#Word guess in this format :_ _ _ _ 
for char in word:
    word_guess.append("_")



while not end_of_game:
  char_guess=input("Guess a letter: ").lower()
  # clear()

  for pos in range(len(word)):
      if char_guess == word[pos]:
          word_guess[pos]=char_guess
  
  print(f"{' '.join(word_guess)}")

  if char_guess not in word_guess:
    lives -= 1
    print(stages[lives])
    if lives == 0 :
      end_of_game= True
      print("GAME OVER")
  
  if "_" not in word_guess:
    end_of_game= True
    print("YOU WIN")

