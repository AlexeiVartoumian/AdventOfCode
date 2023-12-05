"""
--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
"""

"""
Because the input sizes are massive its not feasible to generate a numbered array representing this new range.
Im thinking instead to go about this by representing this range as an interval itself and if any number belonging to this
interval fits into my key:val pairs of intervals then return the smallest one out of them. 
"""
import time
from collections import defaultdict
filepath = "input.txt"

seeds = []

s2Soil= defaultdict(list)
s2Fertilzer = defaultdict(list)
f2water = defaultdict(list)
w2light= defaultdict(list)
l2temperature= defaultdict(list)
t2humidity = defaultdict(list)
h2location = defaultdict(list)
mappings = [s2Soil,s2Fertilzer,f2water,w2light,l2temperature,t2humidity,h2location]
first = True
count = -1
with open(filepath, "r") as file:
    linecount  = 1
    for line in file:
        if first:
            input = line.strip()
            input = line.split(" ")
            input = input[1::]
            
            input = " ".join(input)
            input= input.strip()
            input = input.split(" ")
            
            first = False
            for i in input:
                seeds.append(int(i))
        else:
            
            if line.isspace():
                linecount  = 1
                continue
            else:
                #print(line)
                input = line.split(" ")
                input = " ".join(input)
                input = input.strip()
                input = input.split(" ")
                # input= input.strip()
                # input = input.split(" ")
                if "map:" in input:
                    count+=1
                else:
                   
                    
                    interval = [int(input[1]), int(input[1])+ int(input[2])-1]
                    Dvalue = int(input[0])
                    mappings[count][linecount].append( interval)
                    mappings[count][linecount].append( Dvalue)
                    linecount+=1


print(seeds , mappings)
locationvalues = []
"""
how to read for my own reference
what Im iterating through: taking the seed-to-soil-map I converted it into the following structure
{1: [[98, 99], 50], 2: [[50, 97], 52]})
[98,99] is the range and the 50 is the lowest value corresponding to lower bound of range.
in this case 50 : 98 and all numbers inclusive of upper bound.
for line 2 : range is 50 : 97  and 50 maps to 52. given a seed value of 79 it will not fall in the first interval
but will fall in the second interval therefore 79 maps to 81
"""
value =2043754183 
value1 = 4501055
start_time = time.time()
for i in range(value, value + value1):

    change = i

    #print(change , " is now")
    for Almanac in mappings:
        possiblevalues = []
        notinInterval = True
        for j , x in Almanac.items():
            
            if change >= x[0][0] and change <= x[0][1]:
                notinInterval= False
                val = change - x[0][0] +x[1]
                possiblevalues.append(val)
        
        #if i == 1:
            
        if not possiblevalues:
            possiblevalues.append(change)
        #print(possiblevalues,Almanac)
            
        change = min(possiblevalues)
    locationvalues.append(change)
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the result
print(f"Elapsed time: {elapsed_time} seconds")

#print(locationvalues)

print(min(locationvalues))