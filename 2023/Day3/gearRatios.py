"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""
"""
first thing I want to do is to turn my input into a list.then Im thinking I want to to 8-way dfs on each cell around a symbol and add all tuples that are digits. kind of hackey but once done. I loop through the entire grid again. and now ask the question is tuple in my set? if so then from that tuple point go left and go right until bound
or period is seen to get the number. this will be in string form until left and right of digit has been explored. turn into an int and I have a number adjacent to a symbol 
"""

filepath = "input.txt"

matrix = []
symbols = {'-', '@', '/', '$', '*', '#', '%', '+', '&', '='}
with open(filepath, "r") as file:

    for line in file:
        
        matrix.append(list(line)[:-1:])
       


height = len(matrix)
width = len(matrix[0])

indexes= set()
directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]

def dfs(i,j,indexes):
    for d in directions:
        xcord = i + d[0]
        ycord= j + d[1]

        if xcord >= 0 and xcord < height and ycord >=0 and ycord < width:
            if matrix[xcord][ycord].isdigit():
                indexes.add((xcord,ycord))
    return indexes

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        
        if matrix[i][j] in symbols:
            indexes = dfs(i,j,indexes)

visited = set()
#print(indexes)
numbers= []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):

        if (i,j) in indexes and (i,j) not in visited:
            string = matrix[i][j]
            
            ycord = j
            while ycord-1 > 0  and matrix[i][ycord-1].isdigit(): # go left
                ycord-=1
                string = matrix[i][ycord] + string
                visited.add((i,ycord))
            ycord = j
            while ycord+1 < width  and matrix[i][ycord+1].isdigit():
                ycord+=1
                string = string + matrix[i][ycord]
                visited.add((i,ycord))
            numbers.append(int(string))

result = sum(numbers)