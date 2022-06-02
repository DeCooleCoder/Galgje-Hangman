import random

#woordlist
woordlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def getthawoord():
  woord = random.choice(woordlijst)
  return woord.upper() 
#alle letters woorden in uppercase gezet voor beter leesbaareid

def Intro():
  print("-----------------------------")
  print("|                           |")
  print("|       Galgje/Hangman      |")
  print("|                           |")
  print("-----------------------------")
  print("")
  print("    Press enter to play  ")
  input("")

def play(woord):
  woord_compleet = "_" * len(woord)
  geraden = False
  geraden_letters = []
  geraden_woorden = []
  tries = 6
  print("Lets play some Hangman!")
  print(display_hangman(tries))
  print(woord_compleet)
  print("\n")
  while not geraden and tries > 0:
    guess = input("Please guess a letter or woord: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in geraden_letters:
        print("You have already geraden that letter", guess)
      elif guess not in woord:
        print(guess, "is not in the woord... too bad D:")
        tries -= 1
        geraden_letters.append(guess)
      else:
        print("Nice!", guess, "is in tha woord")
        geraden_letters.append(guess)
        woord_as_list = list(woord_compleet)
        indices = [i for i, letter in enumerate (woord) if letter == guess]
        for index in indices:
          woord_as_list[index] = guess
          woord_compleet = "".join(woord_as_list)
          if "_" not in woord_compleet:
            geraden = True
    elif len(guess) == len(woord) and guess.isalpha():
      if guess in geraden_woorden:
        print("You already geraden this woord", guess)
      elif guess != woord:
        print(guess, "is not tha woord")
        tries -= 1
        geraden_woorden.append(guess)
      else:
        geraden = True
        woord_compleet = woord
        
    else:
      print("not a valid guess...")
    print(display_hangman(tries))
    print("Guessed letters: ", sorted(geraden_letters))
    print(woord_compleet)
    print("\n")
  if geraden:
    print("Congrats, you geraden the woord! YOU WIN!!!")
  else:
    print("too bad you lost :| The woord was " + woord + " maby next time...")


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
  woord = getthawoord()
  play(woord)
  while input("play again? (Y/N) ").upper() == "Y":
    woord = getthawoord
    play(woord)

if __name__ == "__main__":
  main()