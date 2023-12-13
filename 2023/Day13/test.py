string = """
.###.#..#.###...#
.###......###..#.
....######....##.
##.###..###.##.##
###.##..##.###.#.
###.##..##.###.#.
##.###..###.##.##
....######....##.
.###......###.##.
.###.#..#.###...#
##.#.####.#.##.#.
"""


matrix = [
 ['.', '#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '.', '#'], 
 ['.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.'], 
 ['.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '.'], 
 ['#', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '.', '#', '#'], 
 ['#', '#', '#', '.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '#', '.', '#', '.'], 
 ['#', '#', '#', '.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '#', '.', '#', '.'], 
 ['#', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '.', '#', '#'], 
 ['.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '.'], 
 ['.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '#', '.', '#', '#', '.'], 
 ['.', '#', '#', '#', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '.', '#'], 
 ['#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#', '.']]

hieght = len(matrix)
width = len(matrix[0])
def columns(matrix,width, height):

    for  i in range(width-1):

        tempcol1 = []
        tempcol2= []
        for j in range(height):

            tempcol1.append(matrix[j][i])
            tempcol2.append(matrix[j][i+1])

        #print(tempcol1 ,i, "vs" ,tempcol2, i+1 )
        if tempcol1 == tempcol2:
            print(i, i+1 , "it happend here")
            left = i-1
            right = i+2
            reflection = True
            while reflection and left >= 0 and right <width:
                sorry = []
                sorry2 = []
                for z in range(height):
                    sorry.append(matrix[z][left])
                    sorry2.append(matrix[z][right])
                    #print(matrix[z][left], left, " vs", matrix[z][right], right )
                
                if sorry != sorry2:
                    reflection = False
                left-=1
                right+=1
            if reflection:
                print(left, "vertical reflection babeee", i+1)
                return i+1
    return 0
def rows(matrix,height):

    for i in range(len(matrix)-1):

        row1 =matrix[i]
        row2 = matrix[i+1]
        
        if row1 == row2:
            up = i-1
            down = i+2
            reflection = True
            while reflection and up >= 0 and down < height:
                
                row1 = matrix[up]
                row2 = matrix[down]

                if row1 != row2:
                    reflection = False
                up-=1
                down+=1 

            if reflection:

                print(up , "horizontal reflectrion babbbeee" , abs(i - (-1) ))
                return abs(i - (-1) )
    return 0

print(columns(matrix,width,hieght), rows(matrix,hieght))



string = """
#..##..#..##.
#.####.##.##.
.#.##.#.#....
.#.##.#..####
###..#.#.....
..#..#..##..#
.#.##.#..#..#
"""

matrix2 = []

matrix2.append( (string.split("\n")) )

for i in range(len(matrix2[0])):
    newarr = []
    print(matrix2[0][i])
    
    for j in range(len(matrix2[0][i])):
        newarr.append(matrix2[0][i][j])
    
    matrix2[0][i] = newarr

print(matrix2)

matrix2  = [['#', '.', '.', '#', '#', '.', '.', '#', '.', '.', '#', '#', '.'], 
            ['#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.'], 
            ['.', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '.', '.'], 
            ['.', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#', '#', '#'], 
            ['#', '#', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.'], 
            ['.', '.', '#', '.', '.', '#', '.', '.', '#', '#', '.', '.', '#'], 
            ['.', '#', '.', '#', '#', '.', '#', '.', '.', '#', '.', '.', '#']]