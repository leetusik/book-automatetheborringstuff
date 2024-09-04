import random

print("I am thinking of a number between 1 and 20.")
answer = random.randint(1, 20)
while True:
    response = int(input("Take a guess.\n"))
    if response > answer:
        print("too big.")
    elif response < answer:
        print("too small.")
    else:
        print("good job!")
        break
