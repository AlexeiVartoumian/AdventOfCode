"""
--- Part Two ---
You resume walking through the valley of mirrors and - SMACK! - run directly into one. Hopefully nobody was watching, because that must have been pretty embarrassing.

Upon closer inspection, you discover that every mirror has exactly one smudge: exactly one . or # should be the opposite type.

In each pattern, you'll need to locate and fix the smudge that causes a different reflection line to be valid. (The old reflection line won't necessarily continue being valid after the smudge is fixed.)

Here's the above example again:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
The first pattern's smudge is in the top-left corner. If the top-left # were instead ., it would have a different, horizontal line of reflection:

1 ..##..##. 1
2 ..#.##.#. 2
3v##......#v3
4^##......#^4
5 ..#.##.#. 5
6 ..##..##. 6
7 #.#.##.#. 7
With the smudge in the top-left corner repaired, a new horizontal line of reflection between rows 3 and 4 now exists. Row 7 has no corresponding reflected row and can be ignored, but every other row matches exactly: row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.

In the second pattern, the smudge can be fixed by changing the fifth symbol on row 2 from . to #:

1v#...##..#v1
2^#...##..#^2
3 ..##..### 3
4 #####.##. 4
5 #####.##. 5
6 ..##..### 6
7 #....#..# 7
Now, the pattern has a different horizontal line of reflection between rows 1 and 2.

Summarize your notes as before, but instead use the new different reflection lines. In this example, the first pattern's new horizontal line has 3 rows above it and the second pattern's new horizontal line has 1 row above it, summarizing to the value 400.

In each pattern, fix the smudge and find the different line of reflection. What number do you get after summarizing the new reflection line in each pattern in your notes?
"""

"""
the plan is to introduce a wild card where I sift thorugh every char by column and every char by row. allow only one difference
for each comparison. wild card may only be used once and doesnt neccessarily hvae to be used right away.
"""

filepath = "input.txt"

mirrors = {}
count = 0
mirrors[count] = []
with open(filepath, "r") as file:


    for line in file:
        if len(line) >1:
            
            mirrors[count].append(list(line.rstrip()))
        else:
            count+=1
            mirrors[count] = []


print(mirrors)
def checkindex(curindex, previndex):
    if previndex == None:
        return True
    if previndex == curindex+1:
        return False
    return True

def columns(matrix,width, height, previndex):

    for  i in range(width-1):

        tempcol1 = []
        tempcol2= []
        wildcard = 0
        for j in range(height):

            if matrix[j][i] != matrix[j][i+1]:
                wildcard+=1
            tempcol1.append(matrix[j][i])
            tempcol2.append(matrix[j][i+1])

        if (wildcard <=1 or tempcol1 == tempcol2 ) and checkindex(i, previndex):
            left = i-1
            right = i+2
            reflection = True
            while reflection and left >= 0 and right <width:
                sorry = []
                sorry2 = []
                for z in range(height):
                    if matrix[z][left] != matrix[z][right]:
                        wildcard+=1
                    sorry.append(matrix[z][left])
                    sorry2.append(matrix[z][right])
                if sorry != sorry2 and wildcard >1:
                    reflection = False
                left-=1
                right+=1
            if reflection:
                print(left, "vertical reflection", i+1)
                return i+1
    return 0




def rows(matrix,height ,previndex):
    for i in range(len(matrix)-1):
        wildcard = 0
        row1 = []
        row2 = []
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[i+1][j]:
                wildcard+=1
            row1.append(matrix[i][j])
            row2.append(matrix[i+1][j])
        
        if (row1 == row2 or wildcard <=1) and checkindex(i,previndex):
            up = i-1
            down = i+2
            reflection = True
            while reflection and up >= 0 and down < height:
                
                row1 = matrix[up]
                row2 = matrix[down]
                
                for check in range(len(row1)):
                    if row1[check] != row2[check]:
                        wildcard+=1
                if row1 != row2 and wildcard>1 :
                    reflection = False
                up-=1
                down+=1 
            if reflection:
                print(up , "horizontal reflection " , i+1)
                return i+1
    return 0
#rows(matrix)


runningsum = 0
#res = [{'c': 5}, {'r': 4}]
res = [{'r': 2}, {'r': 3}, {'c': 2}, {'r': 1}, {'r': 14}, {'c': 12}, {'c': 11}, {'c': 7}, {'r': 12}, {'r': 6}, {'r': 2}, {'c': 6}, {'r': 4}, {'c': 7}, {'r': 1}, {'r': 8}, {'c': 12}, {'c': 9}, {'r': 1}, {'r': 2}, {'c': 2}, {'r': 2}, {'r': 2}, {'r': 2}, {'r': 3}, {'r': 8}, {'r': 15}, {'r': 8}, {'c': 2}, {'r': 13}, {'r': 11}, {'r': 1}, {'r': 1}, {'r': 7}, {'c': 7}, {'c': 9}, {'c': 8}, {'c': 2}, {'r': 2}, {'r': 1}, {'r': 2}, {'r': 9}, {'r': 13}, {'c': 12}, {'c': 2}, {'c': 14}, {'c': 12}, {'c': 9}, {'c': 2}, {'c': 2}, {'r': 11}, {'c': 6}, {'c': 8}, {'c': 9}, {'c': 2}, {'r': 10}, {'r': 5}, {'c': 2}, {'r': 12}, {'c': 14}, {'r': 6}, {'r': 2}, {'c': 11}, {'c': 8}, {'r': 1}, {'r': 4}, {'c': 7}, {'r': 10}, {'r': 12}, {'c': 3}, {'c': 16}, {'c': 1}, {'c': 3}, {'c': 8}, {'c': 11}, {'c': 8}, {'c': 1}, {'c': 1}, {'c': 13}, {'r': 6}, {'c': 6}, {'c': 1}, {'r': 16}, {'r': 4}, {'c': 10}, {'r': 2}, {'r': 5}, {'c': 1}, {'r': 1}, {'c': 3}, {'c': 10}, {'c': 10}, {'r': 2}, {'r': 14}, {'c': 11}, {'r': 2}, {'r': 1}, {'c': 11}, {'c': 7}, {'r': 1}]
for i,x in mirrors.items():
    height = len(x)
    width = len(x[0])
    print("-------------------")
    
    if  "r" in res[i]:
        rowcount= rows(x,height, res[i]["r"])
        colcount = columns(x,width,height,None)
    else:
        
        rowcount = rows(x,height,None)
        colcount= columns(x,width, height, res[i]["c"])
    
    if rowcount != 0:
        
        if "r" in res[i]:
            if rowcount != res[i]["r"]:
               
                runningsum+= (100*rowcount)
        else:
            
            runningsum+= (100*rowcount)
        
    if colcount !=0:
        
        if "c" in res[i]:
           
            if colcount != res[i]["c"]:
              
                runningsum += colcount
        else:
           
            runningsum += colcount
   
    print(rowcount , colcount)
    print("-------------------")

print(runningsum)



