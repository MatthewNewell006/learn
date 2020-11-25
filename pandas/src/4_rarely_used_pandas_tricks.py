'''

Groupby with NamedAgg

The groupby function is commonly used in exploratory data analysis.
Combined with the agg function, we are able to apply different aggregation functions to different columns.
The NamedAgg method allows us to rename the aggregated columns inside the agg function.

'''

import numpy as np
import pandas as pd

cats = pd.Series(list('abc') * 3).sample(n = 9).reset_index(drop = True)

df = pd.DataFrame({'A': cats, 'B': np.random.randint(1, 10, size = 9), 'C': np.random.randint(1, 20, size = 9)})
print(df)

print('\n')

'''

I want to group the rows by column A and then take the average on column B and sum on column C.
I also want to rename the aggregated columns to inform about the applied function.

'''

grouped = df.groupby('A').agg(average_B = pd.NamedAgg('B', 'mean'), total_C = pd.NamedAgg('C', 'sum'))
print(grouped)

print('\n')

'''

Groupby with pipe

Using the pipe with groupby allows us to apply function with arguments to the groupby object.

For each value in column B, we want to extract the mean value of the other group.
For example, the first row belongs to group b in column A. So the average value of group a will be subtracted from 9.

'''

df['C'] = df.groupby('A').B.pipe(
    lambda x: (
        x.get_group('a') - x.get_group('b').mean()).append(x.get_group('b') - x.get_group('a').mean()))
print(df['C'])

print('\n')

'''

Where

The where function can be used to update the values of a column based on a condition.
Assume we need to update the values in column B according to the following conditions:
All the values that are less than 5 will be replaced by 5
The other values (5 or higher) will remain the same
This task can be accomplished using the where function:

'''

df['D'] = df['B'].where(df['B'] > 5, 5)
print(df['D'])

print('\n')

'''

You can compare the values between column B and D.
You don’t actually have to create a new column. I created a new column to be able to show a comparison.
The way “where” works is that values that fit the condition are selected and the remaining values are replaced with the specified value.
Note: One important point is that “where” for Pandas and NumPy are not exactly the same.
We can achieve the same result but with slightly different syntax.
With DataFrame.where, the values that fit the condition are selected as is and the other values are replaced with the specified value.
Np.where requires to also specify the value for the ones that fit the condition.
The numpy syntax to do the operation we just did:

'''

print(np.where(df['B'] > 5, df['B'], 0))
print('\n')

'''

Lookup

Lookup function can be used to look up values in a dataframe based on the values on other row, column pairs.
This function is best explained via an example.
Consider the following dataframe.

For each day, we have recorded values for three people.
We also have a column (Names) that assign a name to each day.
We want to create a column that contains the recorded value of the assigned name for each day.


df2['Person_point'] = df2.lookup(df2.index, df2['Names'])

'''

