import random
import os
from time import sleep

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
  os.system('clear')
  woord_compleet = "_" * len(woord)
  geraden = False
  geraden_letters = []
  geraden_woorden = []
  tries = 6
  print("Laten we het potje Galgje maar beginnen!")
  print(display_hangman(tries))
  print(woord_compleet)
  print("\n")
  while not geraden and tries > 0:
    guess = input("raad een letter dat je denkt dat in het woord voorkomt: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in geraden_letters:
        print("Je hebt dat letter al geraden", guess)
      elif guess not in woord:
        print(guess, "is niet in het woord... Jammer D:")
        tries -= 1
        geraden_letters.append(guess)
      else:
        print("Nice!", guess, "is in het woord")
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
        print("Je hebt dit woord al geraden", guess)
      elif guess != woord:
        print(guess, "is niet het woord")
        tries -= 1
        geraden_woorden.append(guess)
      else:
        geraden = True
        woord_compleet = woord
        
    else:
      print("Niet een geldig antwoord")
    print(display_hangman(tries))
    print("Geraden letters: ", sorted(geraden_letters))
    print(woord_compleet)
    print("\n")
  if geraden:
    print("Gefeliciteerd je hebt het woord goed geraden!!! Hier heb een smiley :D")
  else:
    print("Jammer je hebt het fout... het woord was " + woord + " volgende keer beter :|")


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
                  ---
                """,
                # oke je hebt nog een kans
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                  ---
                """,
                # zowat bijna halverwege
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                  ---
                """,
                # je hebt nu al 3 keer gefaald
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                  ---
                """,
                # 2x gefaald
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,
                # 1 keer gefaald
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                """,
                # Humble Beginnings
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                """
    ]
    sleep(1.25)
    os.system('clear')
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