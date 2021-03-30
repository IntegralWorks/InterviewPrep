'''
sort tuples based on nth param: https://stackoverflow.com/questions/8459231/sort-tuples-based-on-second-parameter
convert list into indexed tuple list: https://www.geeksforgeeks.org/python-convert-list-to-indexed-tuple-list/
make random sample: https://www.tutorialspoint.com/generating-random-number-list-in-python
'''
#Question found here: https://www.interviewcake.com/question/python3/stock-price

import random
import pretty_errors

#stock_prices = [10, 7, 5, 8, 11, 9]
def getGreatestReturn(prices):
    l = sorted(list(enumerate(prices)), key = lambda x: x[1])
    while True:
        print(f'processing . . .{l}\n')
        if (l[-1][0] == 0):
            l.pop(-1)#if the price was at the highest from market open, then we disregard it
        if(l[-1][0] > l[0][0]):
            return(l[-1][1] - l[0][1])
        else:
            l.pop(0) #if the lowest price happened after the highest, then we disregard it

#tests: need odd list, even list, list with all the same prices


odd = random.sample(range(1,100),9)
even = random.sample(range(1,100),10)
ones = [1,1,1,1,1]

print(f'{odd} \nyields a sort of {sorted(list(enumerate(odd)), key = lambda x: x[1])} \nresulting in a greatest profit of: {getGreatestReturn(odd)}\n')
print(f'{even} \nyields a sort of {sorted(list(enumerate(even)), key = lambda x: x[1])} \nresulting in a greatest profit of: {getGreatestReturn(even)}\n')
print(f'{ones} \nyields a sort of {sorted(list(enumerate(ones)), key = lambda x: x[1])} \nresulting in a greatest profit of: {getGreatestReturn(ones)}\n')
