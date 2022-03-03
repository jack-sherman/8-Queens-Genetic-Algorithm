import numpy as np
import matplotlib.pyplot as plt
from copy import copy, deepcopy
import random

# Value below is the number of boards in the initial population.
SIZE = 10

Pop = []


def initPop(SIZE):
    # Each array index represents a column on a chess board.
    # index 0 corresponds to column 1 in a chess board.
    # The value at that index corresponds to the row that the queen is placed.
    # index 5 with a value 3 corresponds to column 6 row 3.
    # I don't want to randomly assign values to each index because most randomly generated boards
    # will have multiple queens on the same row. A valid solution will have
    temp = []
    for n in range(SIZE):
        arr = np.arange(1, 9)
        np.random.shuffle(arr)
        temp.append(arr)
    return temp


def calcFitness(arr):
    # all we have to do is check the number of queens attacking each other.
    # There are 8 choose 2 pairs of non-attacking queens in a board state that satisfies
    # the 8 queens problem. Therefore the maximum fitness of any state is 28.
    # Determine the fitness with: 28 - number of attacking pairs.
    # The only attacking pairs we can have with this setup before the crossover is diagonal
    # attackers, but after the crossover we have to check for attackers on the same row as well.
    pairs = 0
    global solved
    # check the diagonals
    for i in range(len(arr)):
        for j in range(len(arr)):
            # make sure we don't compare the same value to itself.
            if i != j:
                diagRow = abs(arr[i] - arr[j])  # to check the distance from row i to row j
                diagColumn = abs(i - j)  # this is to check the distance from column i to column j
                if diagColumn == diagRow:
                    pairs += 1
    # below counts the number of unique row values in the board array. 8 - this number
    # gives us the number of columns with non-unique row numbers.
    pairs += 8 - len(np.unique(arr))
    if pairs == 0:
        solved = 1
    # I kept getting an error from negative probabilities because the fitness would go negative. I fixed this
    # by simply setting fitness value to 0 if pairs > 28.
    if pairs > 28:
        pairs = 28
    return 28 - pairs


def buildFit():
    for board in Pop:
        fitness.append(calcFitness(board))
    tot = 0
    temp = []
    for val in fitness:
        tot += val
    for i in range(len(fitness)):
        temp.append(fitness[i]/tot)
    return temp

def selectParents(SIZE):
    temp = []
    for i in range(SIZE):
        temp.append(np.random.choice(SIZE, 2, replace=False, p=fitnessprob))
    return temp

def redefinePop(parents, mp):
    for i in range(SIZE):
        arr = np.arange(8)
        n = np.random.choice(arr)
        t1 = np.array(Pop[parents[i][0]][:n])
        t2 = np.array(Pop[parents[i][1]][n:])
        temp = np.append(t1, t2)
        t = np.arange(100)
        if np.random.choice(t) < (mp*100):
            i = np.random.choice(np.arange(8))
            j = np.random.choice(np.arange(1, 9))
            temp[i] = j
        Pop[i] = temp

# CHANGE ITERATIONS TO MODIFY THE NUMBER OF TRIALS
iterations = 10
calcs10 = []
calcs100 = []
calcs500 = []
calcs1000 = []
MutationPct = 0.10
for num in range(iterations):
    Pop = initPop(SIZE)
    solved = 0
    ticker = 0
    while solved != 1 and ticker < 20000:
        ticker += 1
        fitness = []
        fitnessprob = buildFit()
        if solved == 1:
            continue
        redefinePop(selectParents(SIZE), MutationPct)
    print("Generation : ", ticker)
    if solved == 1:
        print(Pop[fitness.index(28)])
    else:
        print(Pop[0])

#    calcs10.append(ticker)
    calcs10.append(sum(fitness)/len(fitness))

    SIZE = 100
    Pop = initPop(SIZE)
    solved = 0
    ticker = 0
    while solved != 1 and ticker < 20000:
        ticker += 1
        fitness = []
        fitnessprob = buildFit()
        if solved == 1:
            continue
        redefinePop(selectParents(SIZE), MutationPct)
    print("Generation : ", ticker)
    if solved == 1:
        print(Pop[fitness.index(28)])
    else:
        print(Pop[0])
#    calcs100.append(ticker)
    calcs100.append(sum(fitness)/len(fitness))


    SIZE = 500
    Pop = initPop(SIZE)
    solved = 0
    ticker = 0
    while solved != 1 and ticker < 20000:
        ticker += 1
        fitness = []
        fitnessprob = buildFit()
        if solved == 1:
            continue
        redefinePop(selectParents(SIZE), MutationPct)
    print("Generation : ", ticker)
    if solved == 1:
        print(Pop[fitness.index(28)])
    else:
        print(Pop[0])
#    calcs500.append(ticker)
    calcs500.append(sum(fitness)/len(fitness))

    SIZE = 1000
    Pop = initPop(SIZE)
    solved = 0
    ticker = 0
    while solved != 1 and ticker < 20000:
        ticker += 1
        fitness = []
        fitnessprob = buildFit()
        if solved == 1:
            continue
        redefinePop(selectParents(SIZE), MutationPct)
    print("Generation : ", ticker)
    if solved == 1:
        print(Pop[fitness.index(28)])
    else:
        print(Pop[0])
#    calcs1000.append(ticker)
    calcs1000.append(sum(fitness)/len(fitness))

ma = max(calcs10)
plt.plot(np.arange(iterations), calcs10, '*')
plt.plot(np.arange(iterations), calcs100, 'o')
plt.plot(np.arange(iterations), calcs500, '+')
plt.plot(np.arange(iterations), calcs1000, 's')
#plt.ylabel("Number of generations to find a solution")
plt.ylabel("Average fitness of generation")
plt.xlabel("Iteration number")
plt.ylim(ymin=0)
# plt.ylim(ymax=10000)
plt.ylim(ymax=30)
plt.xlim(xmin=0)
plt.show()

