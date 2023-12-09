from collections import defaultdict
cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

filepath = "input.txt"

rankings  = [5,(1,4),(2,3),(1,1,3),(1,2,2),(1,1,1,2),(1,1,1,1,1)]
strength = {
    'A' :13,
    'K' :12,
    'Q' :11,
    'T' : 10,
    '9': 9,
    '8' : 8,
    '7' : 7,
    '6': 6,
    '5': 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
    'J' : 1
}


def threeplusj( vals,copy):
    
    while vals > 0:
        for card, value in strength.items():
            if card in copy :
                copy[card] +=1
                vals-=1
                break
    return copy
   
def twoj(vals, copy):
    if len(copy) == 2:
        while vals > 0:
            for card, value in strength.items():
                if card in copy and copy[card] >=2 :
                    copy[card] +=1
                    vals-=1
                    break
    else:
         while vals > 0:
            for card, value in strength.items():
                if card in copy :
                    copy[card] +=1
                    vals-=1
                    break
    return copy
def onej(vals,copy):
    if len(copy) ==3:
        while vals > 0:
            for card, value in strength.items():
                if card in copy and copy[card] >=2 :
                    copy[card] +=1
                    vals-=1
                    break
    elif len(copy) ==2:
        while vals > 0:
            for card, value in strength.items():
                if card in copy and copy[card] >=2 :
                    copy[card] +=1
                    vals-=1
                    break
    else:
        while vals > 0:
            for card, value in strength.items():
                if card in copy:
                    copy[card] +=1
                    vals-=1
                    break
    return copy
ranks= defaultdict(list)

hand2bid = defaultdict(int)
bids = defaultdict(int)
handfreqs = defaultdict(dict)
for i in rankings:
    ranks[i] = []

handchars = defaultdict(dict)


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
        
        for i ,x in freqs.items():
            mytuple.append(x)
          
        
        
        mytuple.sort()
        print(mytuple, input[0], freqs)

        if len(freqs) > 1  and 'J' in freqs:
            copy  = freqs.copy()
            vals = freqs['J']
            del(copy['J'])
            print(vals, copy, input[0], mytuple)
            
            if vals == 1:
                copy = onej(vals,copy)
            elif vals == 2:
                copy = twoj(vals, copy)
            elif vals <=5:
                copy = threeplusj(vals,copy)

            #print("------------------------------")
            #print(mytuple, input[0], freqs, copy  )
            mytuple = []
            for i,x in copy.items():
                mytuple.append(x)
            mytuple.sort()
            #print(mytuple,copy, freqs)
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

#print(ranks)
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
count = 1

total = 0
for i in range(len(rankings)-1,-1,-1):
    current = ranks[rankings[i]]
    for j in range(len(current)):
        print(current[j], bids[current[j]] , count)
        total+= bids[current[j]] * count
        count+=1
print(total)

"""
2345A 1
J345A 2
2345J 3
32T3K 5
KK677 7
T3Q33 11
Q2KJJ 13
T3T3J 17
Q2Q2Q 19
2AAAA 23
T55J5 29
QQQJA 31
KTJJT 34
JJJJJ 37
JJJJ2 41
JAAAA 43
2JJJJ 53
AAAAJ 59
AAAAA 61
"""
print(ranks)