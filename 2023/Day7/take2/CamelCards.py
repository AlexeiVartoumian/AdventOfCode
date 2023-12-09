"""
--- Day 7: Camel Cards ---
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
"""

"""
so im thinking the first thing I have to do is to sort each hand accroding to thier rank.
as soon as I do that I will be able to give a numerical value to each hand and sort them by that value.

EDIT: sorting by assigning numerical value is bogus. need to reconsider how to  rank the card values.thinking to make a function
that force mutliplies for each rank i.e KKKJJ = 1000 + 100 KKKQQ = 1000 + 200 basically for each category make a function that will 
sort according to spec
"""
import sys 
from collections import defaultdict
def fives(handchars):

    for card , freqs in handchars.items():
            return strength[card]
def fourofakind(handchars):
    number1= ""
    number2 = ""
    for card , freqs in handchars.items():
        
            if freqs == 4:
                number1 = str(strength[card])
            else:
                number2 = str(strength[card])
    return int(str(number1+ number2))
def fullhouse(handchars):
    number1 = ""
    number2 = ""
    for hand , freqs in handchars.items():
        
            if freqs == 3:
                number1 = str(strength[hand])
            else:
                number2 = str(strength[hand])
    return int(number1 + number2) 
def trips(handchar):
    number1 = 0
    number2 = 0
    number3 = 0
    count = 0

    
   
    for char , freqs in handchar.items():
          
            if freqs == 3:
                number1 = strength[char]
            else:
                if count == 0:
                    number2 = strength[char]
                    count+=1
                else:
                    number3 = strength[char]
    #print(number1,number2, number3 , "hahahahah", hand, freqs)
    return (number1 *10 + min(number2, number3)) * 10 + max(number2,number3)

def twopair(handchar):
    number1 = 0
    number2 = 0
    number3 = 0
    count = 0
    
    for char , freqs in handchar.items():
            
            if freqs != 2:
                #print("oop", char)
                
                number3 = strength[char]
            else:
                if count == 0:
                    number1 = strength[char]
                    
                    count+=1
                else:
                    number2 = strength[char]
    value1 = str(min(number1, number2))
    value2 = str(max(number1,number2))
    value3 = str(number3)
    return int(value1+value2+value3)

def pair(handchar):
    number1 = ""
    number2 = ""
    count = 0
    
    while count < len(handchar):
        for card , value in strength.items():
            if card in handchar:
                if handchar[card] != 2:
                    number2+= str(value)
                    count+=1
                else:
                    number1 = str(value)
                    count+=1
    
    return int(number1 + number2)
def ones(freqs):

    visited= set()
    count = 0
    number = ""
    while count < 5:
        for card , rank in strength.items():
            if card in freqs and card not in visited:
                number+= str(strength[card])
                count+=1
                visited.add(card)
    
    return int(number)
   
cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

filepath = "input.txt"
bids= defaultdict(int)
rankings  = [5,(1,4),(2,3),(1,1,3),(1,2,2),(1,1,1,2),(1,1,1,1,1)]
strength = {
    'A' :10,
    'K' :12,
    'Q' :13,
    'J' : 14,
    'T' : 15,
    '9': 16,
    '8' : 17,
    '7' : 18,
    '6': 19,
    '5': 20,
    '4' : 21,
    '3' : 22,
    '2' : 23
}
values = defaultdict(int)
ranks= defaultdict(list)
for i in rankings:
    ranks[i] = []

handchars = defaultdict(dict)
#step 1 key to bid
with open(filepath, "r") as file:

    for line in file:
        counts = defaultdict(int)
        
        input = line.split(" ")
        input[1] = int(input[1].strip("\n"))
       
        bids[input[0]] = input[1]
        freqs = {}
        totalval = 0
        for j in input[0]:
            freqs[j] = 1 + freqs.get(j,0) 
            totalval+=strength[j]
        mytuple = []

        totalval = 0
        for i ,x in freqs.items():
            mytuple.append(x)
            totalval += x * strength[i]
        
        mytuple.sort()
       
        
        if mytuple == [5]:
            ranks[5].append(input[0])
            #print( input[0],fives(handchars))
            #(2,3),(1,1,3),(1,2,2),(1,1,1,2),(1,1,1,1,1)
            totalval = fives(freqs)
        elif mytuple == [1,4]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
            #print( input[0],fourofakind(handchars))
            totalval = fourofakind(freqs)
        elif mytuple == [2,3]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
            #print( input[0],fullhouse(handchars))
            totalval = fullhouse(freqs)
        elif mytuple == [1,1,3]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
            
            #print( trips(freqs))
            totalval = trips(freqs)
        elif mytuple == [1,2,2]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
            #print("begin", input[0])
            #print( input[0],twopair(freqs))
            #print("this happend", input[0])
            totalval = twopair(freqs)
        elif mytuple == [1,1,1,2]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
           
            #print( input[0],pair(handchars))
            
            totalval = pair(freqs)
        else:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])
            #print( input[0],ones(handchars))
            totalval = ones(freqs)
        values[input[0]] = totalval # im gonna use this for insertion sort
        #handchars[input[0]] = freqs
        handchars[input[0]] = freqs
# print(handchars)
# print(bids)
#print(values)
#print(ranks)



#print(bids)
#print(ranks[(1,4)])

# print(len(bids))

#print(values)
#print(ranks[(1,1,1,1,1)])
# print(bids["JJJJJ"])
#print(ranks[(1,4)])
#print(ranks)
print(ranks)
argh = []
for i in range(len(ranks[(1,1,1,1,1)])):
   
    argh.append( values[ranks[(1,1,1,1,1)][i]])

for rank in rankings:
    for i in range(1,len(ranks[rank])):

        j = i
        
        while j > 0 and values[ranks[(rank)][j]] < values[ranks[(rank)][j-1]]:
            #if rank == (1,4):
                # print(j , j-1 , "indexes")
                # print(values[ranks[(rank)][j]], values[ranks[(rank)][j-1]])
                # print( ranks[(rank)][j],ranks[(rank)][j-1] )
            ranks[rank][j],ranks[(rank)][j-1]  = ranks[rank][j-1], ranks[(rank)][j]
            j-=1
        # if rank == (1,4):
        #     print("end index",j , i )
# print(bids)
#print(ranks)
#print("AFTER")
# print("-------------------------------------")
#print(ranks[(1,1,1,1,1)])
# argh2 = []
# for j in range(len(ranks[(1,1,1,1,1)])):
   
#     argh2.append( values[ranks[(1,1,1,1,1)][j]])
#     #print(ranks[((1,1,1,1,1))][j], values[ranks[(1,1,1,1,1)][j]])
# print(argh)
# print(argh2)

# print(argh)
count = 1

total = 0

#for i in range(len(rankings)-1,-1,-1):
    #print(rankings[i],ranks[rankings[i]])
    
    #for j in range(len(ranks[rankings[i]])-1,-1,-1):
        # print(ranks[rankings[i]][j],values[ranks[rankings[i]][j]],count)
        # print(bids[ranks[rankings[i]][j]])
        # if rankings[i] == (1,4):
        #     print("-------------------------")
        #     print(ranks[rankings[i]][j],values[ranks[rankings[i]][j]],count)
        #     print(bids[ranks[rankings[i]][j]])
        #     print("*************************")
#         total += (bids[ranks[rankings[i]][j]] * count)
#         count+=1
# print(total)

duplicate = 0
with open("output.txt", "a") as file:
    for i in range(len(rankings)-1,-1,-1):
        print(rankings[i],ranks[rankings[i]], file=file)
        print(len(ranks[rankings[i]]), file= file)
        print("@@@@@@@@@@@@@@@@@@@@                 START                @@@@@@@@@@@@@@@@@@@@@@@@@@@", file = file)
        for j in range(len(ranks[rankings[i]])-1,-1,-1):
            print("-------------------------",file=file)
            print("total before", total , file= file)
            print(ranks[rankings[i]][j],values[ranks[rankings[i]][j]],count,file = file)
            print(bids[ranks[rankings[i]][j]],file =file)
            
            total += (bids[ranks[rankings[i]][j]] * count)
            print("total After", total , file= file)
            if  j + 1 < len(ranks[rankings[i]]) and ranks[rankings[i]][j] == ranks[rankings[i]][j+1]:
                duplicate+=1
            else:
                count+=duplicate
                count+=1
                duplicate = 0
                #count+=1
            print("*************************",file = file)
        
        
print(total)
#248491551

#248851687
#249352187
#