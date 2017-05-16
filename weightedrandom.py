# weighted random practice
import random
import sys, os

num_of_choices = 27

from urllib2 import urlopen
data = urlopen(r"http://arczone.esri.com/")
contents = data.readlines()
output = open(os.path.join(os.getcwd(), "numbers.txt"), "w")
for line in contents:
    print("Writing %s to a file" % (line,))
    output.write(line)
    
sys.exit()
# items to be populated from web
items = [12, 22, 9, 24, 27, 21, 15, 18, 1, 19, 3, 26, 10, 16, 5, 25, 20, 6, 7, 4, 11, 23, 8, 13, 14, 17, 2]

weights = []  # subjective
for i in range(num_of_choices):
    if i >= 0 and i < 5:
        weights.append(2)
    elif i >= 5 and i < 10:
        weights.append(3)
    elif i >= 10 and i < 15:
        weights.append(4)
    elif i >= 15 and i < 20:
        weights.append(5)
    else:
        weights.append(6)
        
sum_of_weights = 0
for i in range(num_of_choices):
    sum_of_weights += weights[i]
  
#print sum_of_weights
# sum_of_weights = 112

def getVal():
    rnd = random.randint(1, sum_of_weights)
    print "Random : ", str(rnd)
    for i in range(num_of_choices):
        if rnd < weights[i]:
            print "item number : " , str(i)
            print "Selected number : ", items[i]
            return items[i]
        else:
            rnd -= weights[i]

if __name__ == '__main__':
    getVal()


