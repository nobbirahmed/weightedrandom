# weighted random practice
#
# yet to do - number appearing recently get lower weight
#
import random
import sys, os
from itertools import groupby
import collections

def GetMostFrequentsBySlot(f):
    
    lines = f.readlines()
    
    megas = []
    slot1 = []
    slot2 = []
    slot3 = []
    slot4 = []
    slot5 = []
    
    for i, line in enumerate(lines):
        
        if i < 5:  continue  # exclude first 5 lines of numbers.txt

        numbers = [int(c) for c in line.split()[-6:]]  # get the 6 winning numbers
        
        slot1.append(numbers[0])
        slot2.append(numbers[1])
        slot3.append(numbers[2])
        slot4.append(numbers[3])
        slot5.append(numbers[4])
        megas.append(numbers[5])
        #print(numbers)
    
    counter1 = collections.Counter(slot1)
    print(counter1.most_common(15))
    counter2 = collections.Counter(slot2)
    print(counter2.most_common(15))
    counter3 = collections.Counter(slot3)
    print(counter3.most_common(15))
    counter4 = collections.Counter(slot4)
    print(counter4.most_common(15))
    counter5 = collections.Counter(slot5)
    print(counter5.most_common(5))
    counter_mega = collections.Counter(megas)
    print(counter_mega.most_common(15))
    print("I am here")
    
    
first = [9, 6, 1, 28, 2, 9, 20, 16, 6, 1, 9, 16, 3, 3, 17, 7, 9, 3, 10, 1, 3, 10, 4, 9, 2, 4, 23, 3, 20, 2, 5, 4]

first10 = first[:10]

def AssignWeight(f):
    
    lines = f.readlines()
    
    draw = 0  # most recent draw
    
    for i, line in enumerate(lines):
        
        if i < 5: continue  # exclude first 5 lines of numbers.txt
        
        numbers = [int(c) for c in line.split()[-6:]]  # get the 6 winning numbers
        
        if draw < 16: # first 15 draws - prob 0.33
            print(draw)
            #slot1_num_weight = .25
            #slot2_num_weight = .25
            #slot3_num_weight = .25
            #slot4_num_weight = .25
            #slot5_num_weight = .25
            #mega_num_weight = .5   # mega - should be treated differently - pure randomly
          
        elif draw < 33:  # next 17 draws - prob 0.5
            print(draw)
            
        elif draw < 100:  # next 67 draws = prob .75
            print(draw)
            
        else:   # prob 0.92
            print(draw)
            
        draw += 1
        
        
# earlier code in Interest> Python 
if __name__ == '__main__':
    
    f = open("MegaNumbers.txt", "r")
    
    AssignWeight(f)


