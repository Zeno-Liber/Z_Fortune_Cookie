# Todo: Create an ASCII interface

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

  random_num = random.randint(1, 7)

  fortune_list = ["A pleasant surprise is waiting for you just around the corner",
                  "The effort you put in today will quietly pay off later.",
                  "Someone will soon appreciate something you thought went unnoticed.",
                  "A new opportunity will appear when you least expect it.",
                  "Curiosity will lead you somewhere worthwhile.",
                  "The answer you’re looking for will become clear with patience.",
                  "Good fortune favors those willing to try something new."]


  print(fortune_list[random_num])

