# 8-Queens Genetic Algorithm
  The purpose of this project is to solve the 8-queens problem using a genetic algorithm. This project was completed as part of an artificial intelligence course at my university.
This genetic algorithm used different values for the population size of each generation. The fitness function that I used was as gollows: Since there are 8 choose 2 paits of queens that can atttack each other, that means that the maximum fitness any given state can have is 28. The fitness of a specific state is biven by looking at the actual number of pairs of queens that are attacking each other and subtractting 28 by that number of pairs. Queens can attack each other by being on the same row/column or by being on the same diagonals. By design, my program will never have queens on the same column and will not have queens on the same row before crossover. Pairs of queens are randomly selected based on their fitness. The weight of a specific board state is given by taking its fitness and dividing it by the total fitness across an entire generation. The crossover points for each pair are randomly selected as well. The mutation chance is set top 15% currently because I felt that 15% was common enough but not too common. The encoding algorithm that I am using is that board states are represented by a sungle array with 8 indices. Each index corresponds to a column on the board. Each index has an integer that corresponds to the row that the queen would be placed on that column. Below is an example of what the array would look like for a specific board with the array [5,1,8,4,2,7,3,6].

<p align="center">
  <img src="https://user-images.githubusercontent.com/47011094/156489162-3c45f4b0-af15-4bed-8ec1-1630d05ce205.png" />
</p>

The main goal of my program is to test the effect that population size has on the effectiveness of finding a solution quickly. Each time the program is run, population sizes of 10, 100, 500, and 1000 are tried for a number of iterations. The number of generations required to find a solution are graphed against the iteration number.

# Results
<p align="center">
  <img src="https://user-images.githubusercontent.com/47011094/156489337-ead56ef7-f864-4db0-bc9a-5bb77e99473d.png" />
</p>
As seen abolve, the number of iterations over 10 trials seems to show that lower population leads to a larger variance and average number of generations required in order to find a solution. The reason that the points for population = 10 are not on the graph is because they were all consistently over 10,000. It seemed that the population 100 group was consistently finding a solution within 1 or 2 generations.
<p align="center">
  <img src="https://user-images.githubusercontent.com/47011094/156489537-7593c841-c00c-44e2-aa9c-d1f2319029e1.png" />
</p>
Above is the graph of average fitness for each trial. As seen, the average fitness for population = 1000 is very consistent, but lower than the rest. These two graphs show the tradeoff between average fitness and number of generations when it comes to popuilation size. The higher the population size, the higher the average fitness. The higher the population size, the lower the average number of generations needed to find a solution. 

In conclusion, I think for this problem, an appropriate population size to find a solution would be 500 or 1000. While running the python program, it seemed low population would result in high run times and low efficiency. Below are a few examples of solutions found with different population sizes.

<p align="center">
  <img src="https://user-images.githubusercontent.com/47011094/156489791-90741af5-105f-442c-9b90-27ace95e5ee8.png" />
</p>

