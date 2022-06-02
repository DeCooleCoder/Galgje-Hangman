import random

woordlist = ["informatica", "informatiekunde", "spelletje", "spelletje", "aardigheidje", "sholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def getthaword():
  word = random.choice(woordlist)
  return word.upper() 
#alle letters worden in uppercase gezet voor beter leesbaareid

def play(word):
  word_compleet = "_" * length(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6




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



#Game engine
def game():
  print("yay! you won!")
  again = input("Play again? (y/n)")
  # als je wil, nog een keer spelen
  if again == "y":
    game()
  else:
    print("THE END")

game()