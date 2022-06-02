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