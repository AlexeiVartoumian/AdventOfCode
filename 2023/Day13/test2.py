m2 = [
    ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#'], 
    ['.', '.', '.', '.', '#', '.', '#', '#', '#', '#', '.', '#', '.'], 
    ['.', '.', '#', '#', '.', '#', '.', '#', '#', '.', '#', '.', '#'], 
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'], 
    ['.', '.', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#'], 
    ['#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
    ['.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#'], 
    ['.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.'], 
    ['#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#'], 
    ['.', '.', '#', '.', '.', '.', '#', '#', '#', '#', '.', '.', '.'], 
    ['.', '.', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#'], 
    ['.', '.', '.', '.', '#', '.', '#', '.', '#', '#', '.', '#', '.'], 
    ['#', '#', '#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.']]
height = len(m2)
width = len(m2[0])
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

        #print(tempcol1 ,i, "vs" ,tempcol2, i+1 , wildcard )
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
                print(left, "vertical reflection babeee", i+1)
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
        #print(row1, i,"vs", row2, i+1)
        if (row1 == row2 or wildcard <=1) and checkindex(i,previndex):
            up = i-1
            down = i+2
            reflection = True
            while reflection and up >= 0 and down < height:
                
                row1 = matrix[up]
                row2 = matrix[down]
                print(row1, up,"vs", row2, down)
                for check in range(len(row1)):
                    if row1[check] != row2[check]:
                        wildcard+=1
                if row1 != row2 and wildcard>1 :
                    reflection = False
                up-=1
                down+=1 
            if reflection:
                print(up , "horizontal reflectrion babbbeee" , i+1)
                return i+1
    return 0
rows(m2, height,None)
columns(m2, width ,height,1)