import random

def randomArrayGenerator(n):
    return list(set(random.randint(1, 10000) for i in range(n+1)))