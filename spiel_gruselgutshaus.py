# Text-Based Advemture Game
# Your goal is to reach the garden and flee

# making the rooms

# diamond room
def garden():
  # some prompts
  print("\nYou are now in a bright garden!")
  print("And there are some flowers too!")
  print("What would you do? (1 or 2)")
  print("1). Take some flowers and run away.")
  print("2). Just run away.")
  
  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("They were poisoned flowers! The moment you touched it, you fall in a deep hole and you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are an honest man! Congrats you are free now! You won the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")


# bear room
def dining_room():
  # give some prompts
  # '\n' is to print the line in a new line
  print("\nYou are in a dining room now.")
  print("Behind that room is another door.")
  print("You are very thirsty and take notice of a bottle with some liquid in !")
  print("What would you do? (1 or 2)")
  print("1). Take the liquid.")
  print("2). Leave the liquid.")

  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead!
    game_over("The liquid killed you.")
  elif answer == "2":
    # lead him to the diamond_room()
    print("\nVery good, you remain steadfast . You can go through the door now!")
    garden()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type a number?")


# monster room
def kitchen_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the kitchen!")
  print("There a chicken is cooked in a big pot. \nWhat would you do? (1 or 2)")
  print("1). Go back to the hall silently.")
  print("2). You eat some chicken")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the dining_room()
    start()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The chicken is too hot for you, you burn to death.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()








def start():
  # give some prompts.
  print("\nYou are standing in a dark hall.")
  print("There is a door to your left and right, which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to dining_room()
    dining_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to kitchen_room()
    kitchen_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()