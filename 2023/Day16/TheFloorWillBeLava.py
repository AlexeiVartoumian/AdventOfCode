"""
--- Day 16: The Floor Will Be Lava ---
With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.

Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.

Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).

The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.

You note the layout of the contraption (your puzzle input). For example:

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

If the beam encounters empty space (.), it continues in the same direction.
If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.

In the above example, here is how the beam of light bounces around the contraption:

>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..
Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

######....
.#...#....
.#...#####
.#...##...
.#...##...
.#...##...
.#..####..
########..
.#######..
.#...#.#..
Ultimately, in this example, 46 tiles become energized.

The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?
"""

filepath = "input.txt"

matrix = []

with open(filepath , "r") as file:

    for line in file:
        matrix.append( list(line.rstrip()))



"""
if I hit a splitter then explore all the paths until either a new splitter has occurred or it goes out of bounds.
once this happens mark that splitter as visited. in the case a splitter has been seen then we know that we encountered a loop
since all paths of that splitter have been explored.
"""
print(matrix[0][5])
coordinates ={
    "U" : (1,0),
    "D" : (-1,0),
    "L" : (0,-1),
    "R" : (0,1)
}

directions = {
    ((0,1), "|"): [(1,0), (-1,0)], #R -->going up and down
    ((0,-1), "|"): [(1,0), (-1,0)],#L -->going up and down
    ((-1,0), "|"): [(-1,0)],#D
    ((1,0) ,"|") : [(1,0)], # U
    ((-1,0), "-"): [(0,1),(0,-1)],#D -->going left and right
    ((1,0), "-"): [(0,1),(0,-1)], #U -->going left and right
    ((0,-1), "-"): [(0,-1)],#L
    ((0,1), "-"): [(0,1)],#R
    ((-1,0), "/"): [(0,1)],#
    ((1,0), "/"): [(0,-1)],#U
    ((0,-1), "/"): [(1,0)],#L
    ((0,1), "/"): [(-1,0)],#R
    ((-1,0), "\\"): [(0,-1)],#D
    ((1,0), "\\"): [(0,1)],#u
    ((0,1), "\\"): [(1,0)],#R
    ((0,-1), "\\"): [(-1,0)],#L
}
symbols = {"|","-","/","\\"}
number = set()
height = len(matrix)
width = len(matrix[0])


matrixcopy = [row[:] for row in matrix]
from collections import deque

def inbounds(i,j):
    if i >= 0 and i < height and j  >= 0 and j < width:
        return True
    return False

i = 0
j = 0
queue = deque()
if matrix[0][0] == ".":
    trajection = [(i,j) , (0,1)]
    queue.append(trajection)
else:
    nextvalue = ((0,1), matrix[0][0])
    for vals in range(len(directions[nextvalue])):
        xcord = directions[nextvalue][vals][0] 
        ycord = directions[nextvalue][vals][1] 
        if inbounds(xcord, ycord):
            nextone = (xcord,ycord)
            matrixcopy[xcord][ycord] = "#"
            number.add((xcord,ycord))
            newtrajection=[nextone,directions[nextvalue][vals]]
            queue.append(newtrajection)
print("starting", queue)
    
matrixcopy[0][0] = "#"


visited = set()

number.add((0,0))
while queue:
    traverse = len(queue)
    for ride in range(traverse):
        trajection = queue.popleft()
        i, j = trajection[0]
        print("trajefction",trajection , matrix[i][j] )
        if matrix[i][j] in symbols:
            prevvalue = (trajection[1], matrix[i][j] , (i,j))
            nextvalue = (trajection[1], matrix[i][j] )
            print("current: ", prevvalue , "------",visited )
            if prevvalue not in visited:
                    visited.add(prevvalue)
                    for vals in range(len(directions[nextvalue])):
                        xcord = directions[nextvalue][vals][0] + trajection[0][0]
                        ycord = directions[nextvalue][vals][1] + trajection[0][1]
                        if inbounds(xcord, ycord):
                            nextone = (xcord,ycord)
                            matrixcopy[xcord][ycord] = "#"
                            number.add((xcord,ycord))
                            newtrajection=[nextone,directions[nextvalue][vals]]
                            queue.append(newtrajection)
        else:
            i+= trajection[1][0]
            j+= trajection[1][1]
            if inbounds(i,j):
                
                number.add((i,j))
                matrixcopy[i][j] = "#"
                queue.append([(i,j) , trajection[1]])
                



print(len(number))








        
