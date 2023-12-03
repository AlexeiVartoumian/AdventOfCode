"""
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

"""
so kind of the same thing but this time I only care about numbers adjacent to "*". I dont know if its only ever two numbers im multiplying for
or not so im going with same approach only this time associate each star with its own group. what this means is storing the index
of (i,j) where i,j is the index of star as a key , I  will associate all potential numbers as found with that index. then same again generate numbers accounting for consecutive indexes that form the same number then generate product and add it to result keep do till done and bingo.
"""
from collections import defaultdict
from functools import reduce
from operator import mul
filepath = "input.txt"

matrix = []

with open(filepath, "r") as file:

    for line in file:
        matrix.append(list(line)[:-1:])

height = len(matrix)
width = len(matrix[0])

indexes= set()
directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

groups = defaultdict(list)
def dfs(i,j,indexes):
    for d in directions:
        xcord = i + d[0]
        ycord= j + d[1]

        if xcord >= 0 and xcord < height and ycord >=0 and ycord < width:
            if matrix[xcord][ycord].isdigit():
                indexes.append((xcord,ycord))
    return indexes

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        
        if matrix[i][j] == "*":
            potentialproduct = dfs(i,j,[])
            #filter all prodcuts that only have one digit adjacent to it
            if len(potentialproduct) >1:
                groups[(i,j)]= potentialproduct 
            

visited = set()
numbers = {}
runningsum = 0
result = defaultdict(list)

for i, x in groups.items():

    numbers = []
    string = ""
    for j in range(len(x)):
        if  x[j] not in visited:
            xcord = x[j][0]
            ycord = x[j][1]
            string = matrix[xcord][ycord]
            visited.add((xcord,ycord))
            #generate number left and right
            while ycord-1 > 0  and matrix[xcord][ycord-1].isdigit(): # go left
                ycord-=1
                string = matrix[xcord][ycord] + string
                visited.add((xcord,ycord))
                
            ycord = x[j][1]
            while ycord+1 < width  and matrix[xcord][ycord+1].isdigit():
                ycord+=1
                string = string + matrix[xcord][ycord]
                
                visited.add((xcord,ycord))

            numbers.append(int(string))
    
    if len(numbers)>1:
        runningsum += reduce(mul, numbers)
        result[i] = numbers
print(result)
print(runningsum)
