import random
import random
import os, sys
from collections import defaultdict

def excluded_fives(fives):
    
    first_ten = []
    next_some = []  # say 20
    for i, five in enumerate(fives):
        if i <= 6:
            first_ten += five
        else:
            for n in five:
                next_some.append(n)
                if len(next_some) > 20:
                    break
                
    d = defaultdict(int)
    for ten in first_ten:
        d[ten] += 1
    
    dups = []
    for k, v in d.items():
        if v > 1:
            dups.append(k)
            
    others = list(set(first_ten) - set(dups))
    #print others
    
    excluded = []
    for i in range(len(others) - 1):
        excluded.append(others[i])
        if len(excluded) > 10:
            break
    #print dups
    return excluded + dups

        
def make_fives(lines):
    fives = []
    for line in lines:
        items = line.split()
        fives_str = items[-6 : -1]
        five = []
        for item in fives_str:
            try:
                n = int(item)
                five.append(n)
            except:
                continue
        if len(five) == 5:
            fives.append(five)
        
    return fives
        
    
def get_megas_list(lines):
    megas = []
    for line in lines:
        items = line.split()
        item = items[len(items) - 1]
        try:
            n = int(item)
            megas.append(n)
        except:
            continue
    
    excludes = []
    for i, m in enumerate(megas):
        if i < 15:
            excludes.append(m)
            
    ex_set = set(excludes)
    all_set = set(range(1, 50))
    
    sample = list(all_set - ex_set)
    
    mega_choice_list = []
    for i in range(20):
        mega_choice_list.append(random.choice(sample))
        
    return mega_choice_list


def select_cycles(excludeds):
    
    all_set = set(range(1, 57))
    ex_set = set(excludeds)
    sample = list(all_set - ex_set)

    cycles = []
    for i in range(100):
        cycle = set()
        for i in range(12):
            cycle.add(random.choice(sample))
            if len(cycle) == 5:
                break
        cycles.append(list(cycle))
        
    return cycles


if __name__ == '__main__':
    in_file = os.path.join(os.getcwd(), "MegaNumbers.txt")
    
    f_in = open(in_file)
      
    lines = f_in.readlines()
    new_lines = []
    for line in lines:
        line = line.strip()
        if len(line) > 0:
            new_lines.append(line)
         
    fives = make_fives(new_lines)

    #f = open("output.txt", "w")
    print "N" * 20
    print get_megas_list(new_lines)
    print "*" * 20
    cycles = select_cycles(excluded_fives(fives))

    for s in cycles:
        x = sorted(s)
        out = ""
        for y in x:
            out = out + str(y) + "\t" 
        print out
        