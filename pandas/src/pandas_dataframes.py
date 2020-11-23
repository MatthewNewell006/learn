import pandas as pd

prices = pd.Series([1,1,2,3,5], index = ['apple', 'pear', 'banana', 'mango', 'jackfruit'])
inventory = pd.Series([10,50,41,22], index = ['pear', 'banana', 'mango', 'apple'])
discount_prices = prices.apply(lambda x: .9 * x if x > 3 else x)

produce = pd.DataFrame({'price': prices, 'discount_price': discount_prices, 'inventory': inventory})

print(produce)
print('\n')

print(produce.describe())
print('\n')

print(produce.loc['pear':, 'price'])
print('\n')

print(produce.iloc[2:, 1])
print('\n')

print(produce.values)
print('\n')

print(produce.iloc[[1,2,3], :])
print('\n')

print(produce['discount_price'])
print('\n')

print(produce.loc[:, produce.max() > 5])
print('\n')

print(produce.loc[produce['price'] == 1, :])
print('\n')

produce['inventory_value'] = produce['inventory'] * produce['price']
print(produce)
print('\n')

print(produce.drop('inventory_value', axis = 1))
print('\n')

print(produce)
print('\n')

produce.drop('inventory_value', axis = 1, inplace = True)
print(produce)
print('\n')

produce.loc[produce.price >=3, 'price'] = 2.50
print(produce)
print('\n')

#========================================================================================================================

import pandas as pd

prices = pd.Series([1,1,2,3,5],
              index=['apple', 'pear', 'banana', 'mango', 'jackfruit'])

inventory = pd.Series([10, 50, 41, 22],
              index=['pear', 'banana', 'mango', 'apple'])

discount_prices = prices.apply(lambda x: .9*x if x>3 else x)

produce = pd.DataFrame({'price':prices,
                        'discount_price':discount_prices,
                        'inventory':inventory})

one_select = produce.loc[['pear', 'jackfruit'], : ]
print(one_select)

print('\n')

produce['clearance_price'] = prices.apply(lambda x: .5 * x)
print(produce)

print('\n')

two_clearance = produce.iloc[3, : ]
print(two_clearance)

print('\n')

one_select = produce.loc[['pear', 'jackfruit']]
print(one_select)

print('\n')

produce['clearance_price'] = prices * 0.5
print(produce)

print('\n')

two_clearance = produce.iloc[3]
print(two_clearance)

print('\n')

produce['discount_percentage'] = (1 - produce['discount_price'] / produce['price']) * 100
print(produce)