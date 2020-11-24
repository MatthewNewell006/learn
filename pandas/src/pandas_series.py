import pandas as pd
import numpy as np

prices = pd.Series([1,1,2,3,5], index = ['apple', 'pear', 'banana', 'mango', 'jackfruit'])

print(prices)
print('\n')

print(prices.describe())
print('\n')

print(prices.loc['apple'])
print('\n')

print(prices.iloc[0:3])
print('\n')

print(prices.loc['banana': ])
print('\n')

# ========================================================================================================================

numeric_labeled = pd.Series(range(10,50,10), index = range(3,7))

print(numeric_labeled)
print('\n')

print(numeric_labeled[3])
print('\n')

print(numeric_labeled.iloc[3])
print('\n')

# ========================================================================================================================

inventory = pd.Series([10,50,41,22], index = ['pear', 'banana', 'mango', 'apple'])

print(inventory)
print('\n')

print(inventory * prices)
print('\n')

# ========================================================================================================================

nonunique_inventory = pd.Series([10,50,41,22,50], index = ['pear', 'banana', 'mango', 'apple', 'apple'])

print(nonunique_inventory)
print('\n')

print(nonunique_inventory * prices)
print('\n')

print(inventory >= 20)
print('\n')

# ========================================================================================================================

print(prices.mean())
print('\n')

print(prices.std())
print('\n')

print(prices.median())
print('\n')

s = prices.values
x = list(filter(lambda x: x%2 == 0, s))
print(s)
print('\n')
print(x)

print('\n')

y = list(map(lambda x: x%2 == 0, s))
print(y)

print('\n')

# ========================================================================================================================

prices = pd.Series([1,1,2,3,5],
              index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
              index=['pear', 'banana', 'mango', 'apple'])
aligned = prices * inventory
one_ind = inventory.iloc[1:4:2]
two_less = prices.loc[lambda x: x < prices.mean()]
three_onhand = aligned.loc['mango']


print(inventory)
print('\n')

print(prices)
print('\n')

print(aligned)
print('\n')

print(one_ind)
print('\n')

print(prices.mean())
print('\n')

print(two_less)
print('\n')

print(three_onhand)
print('\n')

# ========================================================================================================================

one_ind = inventory[1::2]
two_less = prices.loc[prices < prices.mean()]
three_onhand = (prices * inventory).loc['mango']

print(prices.values)