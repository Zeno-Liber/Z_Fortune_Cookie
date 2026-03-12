# Todo: Refactor from if/else statements into a list matched to index for randint

import random

print("Thank you for eating at Zeno's Noodle stand!")
print("\n")
print("Here is your fortune cookie and have a pleasant day!")
print("\n")


while True:


  print("\n")
  print("Would you like to open your fortune now? Type '1' for Yes or '2' for no: ")
  choice = input(("Type '1' or '2': "))
  print("\n")

  if choice == '1':
      pass
  elif choice == '2':
      break
  else:
      print("Please select a valid option")
      continue

  fortune = random.randint(1, 7)

  if fortune == 1:
      print("\n")
      print("A pleasant surprise is waiting for you just around the corner.")
  elif fortune == 2:
      print("\n")
      print("The effort you put in today will quietly pay off later.")
  elif fortune == 3:
      print("\n")
      print("Someone will soon appreciate something you thought went unnoticed.")
  elif fortune == 4:
      print("\n")
      print("A new opportunity will appear when you least expect it.")
  elif fortune == 5:
      print("\n")
      print("Curiosity will lead you somewhere worthwhile.")
  elif fortune == 6:
      print("\n")
      print("The answer you’re looking for will become clear with patience.")
  elif fortune == 7:
      print("\n")
      print("Good fortune favors those willing to try something new.")
  else:
      print("\n")
      print("Error: Fortune not found!")

