# weighted random practice
import random
import sys

num_of_choices = 49
print "1"
# items to be populated from web
items = [46, 29, 40, 12, 22, 47, 39, 9, 24, 41, 27, 33, 21, 15, 18, 1, 48, 38, 19, 32, 3, 44, 26, 30, 10, 42, 16, 5, 25, 20, 6, 49, 38, 7, 43, 4, 34, 35, 11, 31, 23, 8, 37, 13, 14, 17, 2, 36, 28, 45]
print "2"
weights = []  # subjective
for i in range(num_of_choices):
    if i >= 0 and i < 7:
        weights.append(1)
    elif i >= 7 and i < 12:
        weights.append(3)
    elif i >= 12 and i < 18:
        weights.append(4)
    elif i >= 18 and i < 31:
        weights.append(5)
    elif i >= 31:
        weights.append(6)
    else:
        weights.append(7)
print "3" 
sum_of_weights = 0
for i in range(num_of_choices):
    sum_of_weights += weights[i]
print "4"
#print "Sum of weights:", sum_of_weights
# sum_of_weights = 112

def getVal():
    rnd = random.randint(1, sum_of_weights)
    #print "Random : ", str(rnd)
    for i in range(num_of_choices):
        if rnd < weights[i]:
            #print "item number : " , str(i)
            #print "Selected number : ", items[i]
            return items[i]
        else:
            rnd -= weights[i]
print "5"
def getSix():
    #six_vals = set()
    #rand = getVal()
    flag = False
    i = 1
    while not flag:
        i += 1
        if i > 6:
            flag = True
    #while rand and len(six_vals) < 6:
        #six_vals.add(rand)
    #return list(six_vals)
print "6"
if __name__ == '__main__':
    for i in range(2):
        print str(i)
        x = getSix()
        #y = x.sort()
        #print y


