'''

Rationale

It is often the case that you will have two or more separate, but related, datasets that can be usefully combined together.
One way of performing this operation would be to put the data into tables in a SQL database and then write a JOIN query.
Alternatively, you could use Pandas, which can perform SQL-like joins, and more.

'''

'''

Concatenating DataFrames

The most basic way to combine DataFrames is to simply stack them together. You can use pd.concat to do so.

'''

import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

frames = [df1, df2, df3]

result = pd.concat(frames)
print(result)

print('\n')

print(pd.concat(frames, axis = 1))

print('\n')

'''

Merging DataFrames

For more complex ways of combining DataFrames, pd.merge has a great deal of flexibility.
It allows SQL-style joins that can use either columns or indexes or a combination of both.

'''

left = pd.DataFrame({'key': ['dog', 'cat', 'fish', 'bird'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['bird', 'fish', 'cat', 'dog'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.merge(left, right, on='key')

print(result)

print('\n')

left = pd.DataFrame({'city': ['Springfield', 'Springfield', 'Dover', 'Chicago'],
                                              'state': ['IL', 'OH', 'DE', 'IL'],
                                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                                  'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'city': ['Cleveland', 'Dover', 'Springfield', 'Chicago'],
                                             'state': ['OH', 'NH', 'IL', 'IL'],
                                                 'C': ['C0', 'C1', 'C2', 'C3'],
                                                 'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left, right, on = ['city', 'state']))

print('\n')

'''

Notice that merge defaults to an inner join, but other types of joins can be specified with the how keyword.
(Hint: read the DataFrame merge documentation to learn about 'how', as it may be useful soon...)

Both the merge and concat functions have many options to allow a wide-range of possible merges.
For many more examples, consult Pandas Merging Tutorial , which is the definitive resource for merging functionality.

'''

'''

Join the DataFrames below to return a new DataFrame of users with listed birthdays, along with their addresses if you have them.
The resulting dataframes should include all of the names and birthdays from dobs even if you don't have a corresponding address.
Individuals which are only in the addresses dataframe should only be included if they are also in the dobs dataframe.

'''

dobs = pd.DataFrame({'name': ['Suzy', 'Wei','Yulia', 'Arvind'],
                   'day': ['12', '19', '2', '23'],
                   'month': ['Dec', 'Nov', 'May', 'Jul']})

addresses = pd.DataFrame({'name': ['Marisol', 'Arvind','Stephan', 'Suzy'],
                     'city': ['San Francisco', 'Denver', 'Austin', 'Seattle'],
                     'state': ['CA', 'CO', 'TX', 'WA']})


birthday_address = pd.merge(dobs, addresses, on = 'name', how = 'left')

print(dobs)
print('\n')

print(addresses)
print('\n')

print(birthday_address)
print('\n')

'''

The common column between the two DataFrames is "name", so that's what you merge on.
In order to return all users who have listed birthdays, you need a left merge (since dobs is listed first).

'''

