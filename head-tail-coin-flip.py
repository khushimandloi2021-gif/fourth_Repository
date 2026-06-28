import random

guess = input("Enter Head or Tail: ")
result = random.choice(["Head", "Tail"])
if guess.lower() == result.lower():
    print("You won! 🎉")
else:
    print("You lost! Result was:", result)