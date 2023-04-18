import random

N = 10000
guess = []
for _ in range(N):
    l = list(range(1, 26))
    random.shuffle(l)
    chosen = random.randint(1, 26)
    for i, item in enumerate(l):
        if item == chosen:
            guess.append(i)
            break


print(sum(guess)/len(guess))


guesses = [int(x) for x in open("halfs.txt", 'r').readlines()]
print(sum(guesses)/len(guesses))

import numpy as np

import matplotlib.pyplot as plt
import numpy as np


plt.hist(guesses, density=True, bins=25)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data');
plt.show()