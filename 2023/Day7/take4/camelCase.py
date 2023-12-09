from collections import defaultdict
cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

filepath = "input.txt"

rankings  = [5,(1,4),(2,3),(1,1,3),(1,2,2),(1,1,1,2),(1,1,1,1,1)]
strength = {
    'A' :13,
    'K' :12,
    'Q' :11,
    'J' : 10,
    'T' : 9,
    '9': 8,
    '8' : 7,
    '7' : 6,
    '6': 5,
    '5': 4,
    '4' : 3,
    '3' : 2,
    '2' : 1
}


ranks= defaultdict(list)

hand2bid = defaultdict(int)
bids = defaultdict(int)
handfreqs = defaultdict(dict)
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
        handfreqs[input[0]] = freqs
        totalval = 0
        for i ,x in freqs.items():
            mytuple.append(x)
            totalval += x * strength[i]
        
        mytuple.sort()
       
        
        if mytuple == [5]:
            ranks[5].append(input[0])
            #val2hand[totalval].append(input[0])
        elif mytuple == [1,4]:
            mytuple = tuple(mytuple)
           
            ranks[mytuple].append(input[0])
            
        elif mytuple == [2,3]:
            mytuple = tuple(mytuple)
            ranks[mytuple].append(input[0])            
            
        elif mytuple == [1,1,3]:
            mytuple = tuple(mytuple)
            
            ranks[mytuple].append(input[0])
           
        elif mytuple == [1,2,2]:
            mytuple = tuple(mytuple)
            
            ranks[mytuple].append(input[0])
            
        elif mytuple == [1,1,1,2]:
            mytuple = tuple(mytuple)
            
            ranks[mytuple].append(input[0])
            
        else:
            mytuple = tuple(mytuple)
            #totalval = ones(freqs)
            ranks[mytuple].append(input[0])    
        hand2bid[input[0]] =int(input[1])

# def sortfives(cards):
#     for i in range(1,len(cards)):
#         j = i
#         while j > 0 and strength[cards[j][0]] > strength[cards[j-1][0]]:
#             cards[j], cards[j-1] = cards[j-1], cards[j]
#             j-=1
#     return cards
def sort(cards):
    for i in range(1,len(cards)):
        j = i
        notfound = True
        while j > 0 and notfound:
            #print(cards)
            for char in range(len(cards[j])):
                if strength[cards[j][char]] > strength[cards[j-1][char]]:
                    notfound = False
                    break
                elif strength[cards[j][char]] < strength[cards[j-1][char]]:
                    cards[j], cards[j-1] = cards[j-1], cards[j]
                    j-=1
                    break
            #strength[cards[j][0]] > strength[cards[j-1][0]]
            #cards[j], cards[j-1] = cards[j-1], cards[j]
    return cards

for i in range(len(rankings)-1,-1,-1):

    current = ranks[rankings[i]]
    current = sort(current)
    ranks[rankings[i]] = current
print(ranks)

#print(hand2bid)
#print(handfreqs)
# for rank in rankings:
#     for i in range(1,len(ranks[rank])):
#         j = i
#         while j > 0 and ranks[(rank)][j] > ranks[(rank)][j-1]:
#             ranks[rank][j],ranks[(rank)][j-1]  = ranks[rank][j-1], ranks[(rank)][j]
#             j-=1

count = 1

total = 0
for i in range(len(rankings)-1,-1,-1):
    current = ranks[rankings[i]]
    for j in range(len(current)):
        
        total+= bids[current[j]] * count
        count+=1
print(total)
#249204891 "yaaay"
"""
2345J 3
2345A 1
J345A 2
32T3K 5
Q2KJJ 13
T3T3J 17
KTJJT 34
KK677 7
T3Q33 11
T55J5 29
QQQJA 31
Q2Q2Q 19
2JJJJ 53
2AAAA 23
JJJJ2 41
JAAAA 43
AAAAJ 59
JJJJJ 37
AAAAA 61
"""