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
    
    return (number1 *10 + min(number2, number3)) * 10 + max(number2,number3)

def twopair(handchar):
    number1 = 0
    number2 = 0
    number3 = 0
    count = 0
    
    for char , freqs in handchar.items():
            
            if freqs != 2:
               
                
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

filepath = "input3.txt"
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
val2hand = defaultdict(list)
hand2bid = defaultdict(list)
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
            
           
            totalval = fives(freqs)
            ranks[5].append(totalval)
            val2hand[totalval].append(input[0])
        elif mytuple == [1,4]:
            mytuple = tuple(mytuple)
            totalval = fourofakind(freqs)
            ranks[mytuple].append(totalval)
            val2hand[totalval].append(input[0])
        elif mytuple == [2,3]:
            mytuple = tuple(mytuple)
            totalval = fullhouse(freqs)
            ranks[mytuple].append(totalval)            
            val2hand[totalval].append(input[0])
        elif mytuple == [1,1,3]:
            mytuple = tuple(mytuple)
            totalval = trips(freqs)
            ranks[mytuple].append(totalval)
            val2hand[totalval].append(input[0])
          
        elif mytuple == [1,2,2]:
            mytuple = tuple(mytuple)
            totalval = twopair(freqs)
            ranks[mytuple].append(totalval)
            val2hand[totalval].append(input[0])
        elif mytuple == [1,1,1,2]:
            mytuple = tuple(mytuple)
            totalval = pair(freqs)
            ranks[mytuple].append(totalval)
            val2hand[totalval].append(input[0])   
        else:
            mytuple = tuple(mytuple)
            totalval = ones(freqs)
            ranks[mytuple].append(totalval)
            val2hand[totalval].append(input[0])
           
        values[input[0]] = totalval # im gonna use this for insertion sort
        #handchars[input[0]] = freqs
        handchars[input[0]] = freqs
        hand2bid[input[0]].append(int(input[1]))



# print(hand2bid)
# print(val2hand)
#print(hand2bid)

for rank in rankings:
    for i in range(1,len(ranks[rank])):
        j = i
        while j > 0 and ranks[(rank)][j] > ranks[(rank)][j-1]:
            ranks[rank][j],ranks[(rank)][j-1]  = ranks[rank][j-1], ranks[(rank)][j]
            j-=1

#print(ranks)
#print(val2hand)
#print(hand2bid)
total = 0

multiplier = defaultdict(int)
counts = []
count = 0
#print(len(bids), bids)
for i in range(len(rankings)-1,-1,-1):
    current = ranks[rankings[i]]
    print(current)
    counts.append(count+1)
    count+=1
    for j in range(1,len(current)):
        if current[j] == current[j-1]:
            counts.append(count)
        else:
            counts.append(count+1)
            count+=1
#print(counts)
print(bids)
print(hand2bid)
cur = 0
total = 0
for i in range(len(rankings)-1,-1,-1):
    current = rankings[i]
    for j in range(len(ranks[current])):
        
        hand = ranks[current][j]
        print(val2hand[hand])
        if len(val2hand[hand]) >1:
            
            bid =hand2bid[val2hand[hand].pop()]
        else:
            bid = hand2bid[val2hand[hand][0]]
        print(bid[0], counts[cur])
        total += bid[0] * counts[cur]
        cur+=1
        #print(hand)
print(total)
#for i in range(len(rankings)-1,-1,-1):
     
# for i in range(len(rankings)-1,-1,-1):
    
#     duplicates = 0
#     print("start")
#     print(ranks[rankings[i]])
#     for j in range(len(ranks[rankings[i]])-1,-1,-1):
#         if j < len(ranks[rankings[i]])-1 and ranks[rankings[i]][j] == ranks[rankings[i]][j+1]:
#             duplicates+=1
#             #print(ranks[rankings[i][j]], "hahahahahaah")
#             hand = val2hand[ranks[rankings[i]][j]].pop()
            
#             if not val2hand[ranks[rankings[i]][j]]:
#                 del(val2hand[ranks[rankings[i]][j]])
#             actualbid = hand2bid[hand].pop()
#             if not hand2bid[hand]:
#                 del(hand2bid[hand])
#             print(hand , count, count,actualbid,ranks[rankings[i]][j], hand2bid[ranks[rankings[i]][j+1]])
#             #total += (val2hand[ranks[rankings[i]][j]] * count)
#             total += actualbid * count
#         else:
#             #print(val2hand[ranks[rankings[i]][j]], "hahahaha")
            
#             hand = val2hand[ranks[rankings[i]][j]].pop()
            
#             if not val2hand[ranks[rankings[i]][j]]:
#                 del(val2hand[ranks[rankings[i]][j]])
#             actualbid = hand2bid[hand].pop()
#             if not hand2bid[hand]:
#                 del(hand2bid[hand])
            
#             print(hand , count, count,actualbid)
#             #total += (val2hand[ranks[rankings[i]][j]] * count)
#             total += actualbid * count
#             count+=duplicates
#             count +=1
            
            
#             dupicates = 0
# print(total)

# print(hand2bid)
# print(val2hand)
#6592