"""
You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
"""

"""
As always there is a trick wher it pays to read to the question! im thinking for sure that I want to create an adjacency for each node
but because I am bound by the directions all I have to do is to traverse the adjacency according to the input LLR for example and keep track of the steps taken.
"""

from collections import defaultdict



adjacency = defaultdict(tuple)

filepath= "input.txt"
directions= []
with open(filepath , "r") as file:

    count = 0
    for line in file:
        if count == 0:
            directions = [char for char in line][:-1:]
            count += 1
        else:
            input = line.split("=")
            key = input[0].rstrip()
            
            vals = input[1][1:-1:].split(",")
            
            left = vals[0][1::]
            right = vals[1][1:-1:]
           
            key.strip()
            left.strip()
            right.strip()
            adjacency[key] = (left,right) 
        
    #print(directions)

print(adjacency)
print(directions)


steps = 0
current = "AAA"
found = False

while not found:
    curd =  directions[ steps % len(directions) ]
    steps+=1
    print(adjacency[current],current,steps)
    if curd == "L":
        if adjacency[current][0] == "ZZZ":
            found = True
            
        else:
            current = adjacency[current][0] 
    else:
        if adjacency[current][1] == "ZZZ":
            found = True
            
        else:
            current = adjacency[current][1]
print(steps)


#68322908537401
#4577634872005867




