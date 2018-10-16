'''
Created on Oct 6, 2018

@author: SavvyJack
'''
import itertools

a = [{'a': '1'}, {"c": [1,2,4]}]
b = [{"c": [1,2,3]}, {'a': '1'}]

a_minus_b = [item for item in a if item not in b]
b_minus_a = [item for item in b if item not in a]
sym_diff = list(itertools.chain(a_minus_b,b_minus_a))

print(a_minus_b)
print(b_minus_a)
print(sym_diff)
