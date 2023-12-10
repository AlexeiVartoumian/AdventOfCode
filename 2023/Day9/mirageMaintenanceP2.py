"""
--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
"""


filepath = "input.txt"

sequences= []

with open(filepath, "r") as file:

    for line in file:

        thing = list(map(int , line.split(" ")))
        
        sequences.append(thing)


# runningsum = 0
# for i in range(len(sequences)):
#     sequence = sequences[i]
#     allzeroes = False
#     pyramid = [sequence]
    
#     while not allzeroes:
#         temp = []
#         consecutive = True
#         for j in range(1, len(pyramid[-1])):
#             #print(pyramid[-1][j], pyramid[-1][j-1])
#             if pyramid[-1][j] - pyramid[-1][j-1] != 0:
#                 consecutive = False
#             temp.append(pyramid[-1][j] - pyramid[-1][j-1])
#         pyramid.append(temp)
#         if consecutive:
#             allzeroes = True
        
#     count = 0
#     #print(i,pyramid,"---------------------------------------------------")
#     for total in range(len(pyramid)-1,0,-1):
#         count+= pyramid[total][0] - count
#     print(pyramid[0])
#     print("total is ", pyramid[0][0], "-", count , " = ", pyramid[0][0]-count )
#     runningsum+= (pyramid[0][0] - count)

# print(runningsum)
runningsum = 0
for i in range(len(sequences)):
    sequences[i] = sequences[i][::-1]
    sequence = sequences[i]
    allzeroes = False
    pyramid = [sequence]
    
    while not allzeroes:
        temp = []
        consecutive = True
        for j in range(1, len(pyramid[-1])):
            #print(pyramid[-1][j], pyramid[-1][j-1])
            if pyramid[-1][j] - pyramid[-1][j-1] != 0:
                consecutive = False
            temp.append(pyramid[-1][j] - pyramid[-1][j-1])
        pyramid.append(temp)
        if consecutive:
            allzeroes = True
        
    count = 0
    #print(i,pyramid,"---------------------------------------------------")
    for total in range(len(pyramid)-1,0,-1):
        count+= pyramid[total][-1]
    print(pyramid[0])
    print("total is ",count , "+ " , pyramid[0][-1] , " = ", count+ pyramid[0][-1] )
    runningsum+= count+ pyramid[0][-1]

print(runningsum)