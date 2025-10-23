#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
