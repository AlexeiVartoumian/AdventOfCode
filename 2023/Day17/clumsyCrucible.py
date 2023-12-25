"""
--- Day 17: Clumsy Crucible ---
The lava starts flowing rapidly once the Lava Production Facility is operational. As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.

As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!

You land near the gradually-filling pool of lava at the base of your new lavafall. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.

The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.

To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory. To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.

Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.

For example:

2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)

Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.

One way to minimize heat loss is this path:

2>>34^>>>1323
32v>>>35v5623
32552456v>>54
3446585845v52
4546657867v>6
14385987984v4
44578769877v6
36378779796v>
465496798688v
456467998645v
12246868655<v
25465488877v5
43226746555v>
This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.

Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?
"""

"""
update: I could not figure out why my attempt would override stored values in  matrix copy heat map.
after digging around  and practising on a couple of pathfinding problems turns out I wanted to use a minimum heap . I only want to compute
the smallest cost path trajectory every time first!
"""
"""
so this is a variation of bfs im thinking. where for every starting node I can either go 3 to the left or three to the right.
im thinking for every node so long as it respects the bounds to update the total sum incurred with all of these variations doing a unique bfs for all of those nodes too on the condition that the totalpathvalue is less than current totalpathvalue so long as that totalpathvalue has never been visited. further to this the constraint is that depedning on the direction visited the next possible direction to visit will be the opposite set of orthogonal pairs i.e at start point moving right then on the 1st node visited from right (0,1) the next path can only be up or down by three spaces. the same goes for the opposite. if from (0,1) a right is taken then the right respective to that is to go down, in other words from 0,0 to 0,1 I can go either up or down because I started going from the right
"""

import heapq

matrix = []

filepath = "input.txt"
with open(filepath, "r") as file:
    for line in file:
        matrix.append(list(map(int, list(line.rstrip()))))
    

print(matrix)
height = len(matrix)
width = len(matrix[0])
def inbounds(i,j):
    if i >= 0 and i < height and j >= 0 and j < width:
        return True
    return False
queue = []



directions = [(1,0),(0,1),(-1,0),(0,-1)]
visited = set()

matrixcopy = [ [0] * len(matrix[0]) for row in matrix]
height = len(matrix)
width = len(matrix[0])
matrixcopy[0][0] = matrix[0][0]
visited = set()

queue.append( (0, (3,0),(0,0) ,(1,0)))
queue.append((0, (0,3),(0,0) ,(0,1)))
heapq.heapify(queue)

while queue:

    
    cost, moves , curnode,direction= heapq.heappop(queue)
  
    xcord, ycord = curnode
    xmove , ymove = moves
    # below comment gives least cost to path
    # if curnode == (height-1,width-1):
    #     print(cost)
    #     break
    if xmove != 0 and ( moves,curnode ,direction ) not in visited and inbounds(xcord+direction[0],ycord) :
        xtemp = xcord+direction[0]
        if matrixcopy[xtemp][ycord] == 0:
            matrixcopy[xtemp][ycord] = cost + matrix[xtemp][ycord]
        else:
            #this is how i manage state otherwise its just dijsktras i take the cost relative to previous node and not absolute shortest path
            matrixcopy[xtemp][ycord] = min (cost+ matrix[xtemp][ycord]  , matrixcopy[xtemp][ycord] )
          
            #whatever happens for a given trajectory i store cost + current node value
        for d in directions:
            if (d[0] * -1 , d[1]*-1 ) != direction and d != direction:
                nextvalue = (cost+ matrix[xtemp][ycord], (0,3),(xtemp,ycord),d )
                
                
                heapq.heappush(queue, nextvalue) 
        
        if xmove != -1: 
            nextvalue = (cost+ matrix[xtemp][ycord], (xmove-1,0),(xtemp,ycord),direction )
            
            heapq.heappush(queue, nextvalue) 
        visited.add( (moves, curnode,direction ))
    if ymove != 0 and ( moves,curnode ,direction ) not in visited and inbounds(xcord,ycord+ direction[1]) :
        ytemp = ycord+direction[1]
        if matrixcopy[xcord][ytemp] == 0:
            
            matrixcopy[xcord][ytemp] = cost + matrix[xcord][ytemp]
        else:
            #this is how i manage state otherwise its just dijsktras i take the cost relative to previous node and not absolute shortest path
            matrixcopy[xcord][ytemp] = min (cost+ matrix[xcord][ytemp]  , matrixcopy[xcord][ytemp] )
          
            #whatever happens for a given trajectory i store cost + current node value
        for d in directions:
            if (d[0] * -1 , d[1]*-1 ) != direction and d != direction:
                nextvalue = (cost+ matrix[xcord][ytemp], (3,0),(xcord,ytemp),d )   
                heapq.heappush(queue, nextvalue) 
        if ymove != -1: 
            nextvalue = (cost+ matrix[xcord][ytemp], (0,ymove-1),(xcord,ytemp),direction )
            
            heapq.heappush(queue, nextvalue) 
        visited.add( (moves, curnode,direction ))
print(matrixcopy)


print(matrixcopy)

