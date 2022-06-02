import random

#wordlist
woordlist = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def getthaword():
  word = random.choice(woordlist)
  return word.upper() 
#alle letters worden in uppercase gezet voor beter leesbaareid

def Intro():
  print("-----------------------------")
  print("|                           |")
  print("|       Galgje/Hangman      |")
  print("|                           |")
  print("-----------------------------")
  print("")
  print("    Press enter to play  ")
  input("")

def play(word):
  word_compleet = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Lets play some Hangman!")
  print(display_hangman(tries))
  print(word_compleet)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Please guess a letter or word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
        print("You have already guessed that letter", guess)
      elif guess not in word:
        print(guess, "is not in the word... too bad D:")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Nice!", guess, "is in tha word")
        guessed_letters.append(guess)
        word_as_list = list(word_compleet)
        indices = [i for i, letter in enumerate (word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
          word_compleet = "".join(word_as_list)
          if "_" not in word_compleet:
            guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed this word", guess)
      elif guess != word:
        print(guess, "is not in tha word")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        word_compleet = word
        
    else:
      print("not a valid guess...")
    print(display_hangman(tries))
    print(sorted(guessed_letters))
    print(word_compleet)
    print("\n")
  if guessed:
    print("Congrats, you guessed the word! YOU WIN!!!")
  else:
    print("too bad you lost :| The word was " + word + " maby next time...")


#Poppetje
def display_hangman(tries):
    stages = [  # OOoooo je bent bijna dood o-o
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # oke je hebt nog een kans
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # zowat bijna halverwege
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # je hebt nu al 3 keer gefaald
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # 2x gefaald
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # 1 keer gefaald
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # Humble Beginnings
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


Intro()

#Game engine
def main():
  word = getthaword()
  play(word)
  while input("play again? (Y/N) ").upper() == "Y":
    word = getthaword
    play(word)

if __name__ == "__main__":
  main()