# weighted random practice
#
# yet to do - number appearing recently get lower weight
#
import random
import sys, os
from itertools import groupby
import collections

# earlier code in Interest> Python 
if __name__ == '__main__':
    
    f = open("MegaNumbers.txt", "r")
    
    lines = f.readlines()
    megas = []
    
    slot1 = []
    slot2 = []
    slot3 = []
    slot4 = []
    slot5 = []
    
    for i, line in enumerate(lines):
        
        if i < 5: 
            continue

        numbers = [int(c) for c in line.split()[-6:]]
        
        slot1.append(numbers[0])
        slot2.append(numbers[1])
        slot3.append(numbers[2])
        slot4.append(numbers[3])
        slot5.append(numbers[4])
        megas.append(numbers[5])
        #print(numbers)
    
    counter1 = collections.Counter(slot1)
    print(counter1.most_common(5))
    counter2 = collections.Counter(slot2)
    print(counter2.most_common(5))
    counter3 = collections.Counter(slot3)
    print(counter3.most_common(5))
    counter4 = collections.Counter(slot4)
    print(counter4.most_common(5))
    counter5 = collections.Counter(slot5)
    print(counter5.most_common(5))
    counter_mega = collections.Counter(megas)
    print(counter_mega.most_common(5))
    print("I am here")


