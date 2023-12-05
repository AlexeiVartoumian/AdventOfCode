"""
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

For example:

seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:

50 98 2
52 50 48
The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers looks like this:

seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
With this map, you can look up the soil number required for each initial seed number:

Seed number 79 corresponds to soil number 81.
Seed number 14 corresponds to soil number 14.
Seed number 55 corresponds to soil number 57.
Seed number 13 corresponds to soil number 13.
The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.
"""


"""This question majorly threw me off and my confusion stemmed from how I understood the description at the first pass.
I thought that I should only care about the first two lines of a given almanac category and that all other lines do not matter. further to this i 
understood that these two lines are linked to each other as in the first line is taken input for the second line.
If i think I understood this correctly now each line lives independantly of each other and that that given a number 
I must first determine if it falls into any of the ranges specifically the source range. I should also take into consideration that 
the range value also affects the upper bound to which a given number is bound to.

as such the task is to determine the lowest mapping if it a given number falls into any of these bound and otherwise return the same number to be 
fed into the next category.

as such my first step is to arrange  the D , S , R values into a table where I can readily find the source number and map it to the D avlue.

for each line im thinking of keeping an interval and then asking the question for each line: does source number fall into given interval?
if so then I know  that the number is not allowed to map to itself. after that for each line determine the mapped number 
with the calculation (S+ val + D)  where val is the given number so long as  val >=  S and val <= (S + R -1) which represents the range.
"""

""""
so im going to use the good ol trusty dictionary. i will have eight of them or however many almancs there are.
for each category I will store the following. two lists the first line will be the SOURCE INTERVAL. 
the second list will be the source value to determing where a given value ends up as if it falls in the first interval.

As such once the data has been organised accordingly all i have to do i for each line see it it falls into the range
and at the end of each category pick the smallest number.
"""

from collections import defaultdict
filepath = "input2.txt"

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
change = None
for i in range(len(seeds)):

    change = seeds[i]

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


print(locationvalues)

print(min(locationvalues))