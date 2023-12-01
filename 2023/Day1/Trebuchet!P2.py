"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
"""
so this is janky and theres definitely some super easy way to do this
but im going to process the strings where I ask the question for every string 
does the string version of a given number exist in the string? 
if so grab the starting index of that value as the key and its integer form as the value. I'll also use a list 
to store these indexes so I can sort them as I only care about the first occuring and last occuring number.
the final amendment to do is to still loop through the string and store the index of the first natural and last natural digits.
There are no capital letters in the strings so thats good but even if there was handle that with lower. in the case there is only 
one digit and so long as th guarantee exists as per the test cases that a digit will be in the string then I can have duplicates
in my indexes list I only care about the first and last occuring index.
FORGOTTEN CASE! suppose a worded number occurs more than once where it represents the same digit i.e oneblablaone. index method
will only return first occuring. In this case I will parse an auxilary string that removes first instance of worded number and keep doing so
until no longer found
"""

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four":4,
    "five":5,
    "six": 6,
    "seven":7,
    "eight":8,
    "nine": 9
}

inputs= []

filepath = "input2.txt"

with open(filepath,"r") as file:
     
     for i,x in enumerate(file):
          inputs.append(x.rstrip("\n"))

values = []
outliers = []
#I will comment for my own reference for the jank is strong here
for string in inputs:
    numbervals ={}  # ==> index is key , val is number
    indexes = [] # I will have an index of all worded or intger numbers at end
    output = 0
    for i,x in numbers.items():
        if i in string: # check for word representation of numbers
            numbervals[string.index(i)] = numbers[i] # map index found to integer stored in numbers dicitonary
            indexes.append(string.index(i))

            # the code block below handles the case where the same worded number appears in the string.
            # my appraoch was to slice the string at index of first found worded number
            # replace it with filler of same length and keep processing until that worded number is not in the 
            # amended string filled with "x" placeholders. I need palceholder to maintain the intial index of string.  
            temp = string[:string.index(i):] + "x" * len(i) + string[string.index(i)+ len(i)::]
            if i in temp and i not in outliers:
                 outliers.append(string)
            while i in temp:
                numbervals[temp.index(i)] = numbers[i]
                indexes.append(temp.index(i))
                temp = temp[:temp.index(i):] + "x" * len(i)+temp[temp.index(i) + len(i)::]
    # two pointers scanning left and right for digits
    for j in range(len(string)):
            if string[j].isdigit():
                numbervals[j] = int(string[j])
                indexes.append(j)
                break
    for k in range(len(string)-1,-1,-1):
            if string[k].isdigit():
                numbervals[k] = int(string[k])
                indexes.append(k)
                break
    indexes.sort()
    output=numbervals[indexes[0]]
    output = (output * 10 )+  numbervals[indexes[-1]]
    values.append(output)

total = sum(values)
