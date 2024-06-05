import random

#dictionary of every object you can play (CPU included)
objects = {0: "Rock", 1: "Paper", 2: "Scissors", 3: "Super Soaker"}

#returns a or b depending on the winning index, returns -1 if tie
def calc_win(a, b):
  if a == b:
    return -1

  if a == 3:
    return a
  if b == 3:
    return b

  if b - a == 1:
    return b
  if a - b == 2:
    return b
  return a

#prints every object and its index that you can choose, in a formatted way 
for key, value in objects.items():
  print(value + " = " + str(key))
print(" ")

#Player input
a = int(input("Input Choice: "))
print(" ")

#CPU chooses random index
b = random.randint(0, len(objects) - 1)
print("Player Chooses " + objects[a])
print("CPU Chooses " + objects[b])
print(" ")

#Calculate the winner using the function
winner = calc_win(a, b)
if winner == -1:
  print("Tie game!")
elif winner == a: 
  print("You win!")
elif winner == b:
  print("You lost!")
