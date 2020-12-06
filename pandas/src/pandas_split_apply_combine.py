'''

Splitting data

Like a SQL GROUP BY statement, this is used for things like computing aggregate statistics within groups,
but the Pandas implementation goes considerably beyond what is easily possible in SQL.
This offers much greater flexibility in terms of the expected output of a Pandas groupby operation and what types of computation can be done.

To do group-based computation in Pandas, use the .groupby() method of the DataFrame.
Under simple use, this method simply takes a list of columns whose unique values will form the groups (similar to SQL).
It returns a DataFrameGroupBy object.
This object gives us an interface to apply functionality to the subsets of our data created during splitting.

'''

import pandas as pd

grocery = pd.DataFrame({'category': ['produce', 'produce', 'meat', 'meat', 'meat', 'cheese', 'cheese'],
                        'item': ['celery', 'apple', 'ham', 'turkey', 'lamb', 'cheddar', 'brie'],
                        'price': [.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})

print('\n')

print(grocery)

print('\n') #=====================================================================================================================

print(grocery.describe())

print('\n') #=====================================================================================================================

print(grocery.groupby('category'))

print('\n') #=====================================================================================================================

'''

Applying calculations to groups

There are several methods on the DataFrameGroupBy object.
These methods are all similar in that they have access to some subset of the data determined by the split,
but they differ in the flexibility of return values they allow (for reasons having to do with efficiency).

    aggregate: This method is for operations that return a single value for each group, like mean, or max.
               aggregate iterates over groups and performs its operation on the group as a whole.

    filter: This method is for doing group (not individual row) filtration.
            For example, if you want to eliminate any groups that have too few observations,
            you would first .groupby your DataFrame into groups, then check each group, removing groups that fall below a certain threshold.
            filter will then return every item in the groups that passed.
    
    transform: This method is for operations that return values with the same indices as the original data.
               For example, if you want to center a series by subtracting its mean, you compute the mean,
               then return the original series minus that value. transform iterates over each row and operates on each value individually.

    apply: This method can stand in for any of the above operations, but is less efficient.
           It places no constraints on the type of data returned.

All of these methods take a function that is then applied to each subset of data.
Pandas takes care of the combining part of "split-apply-combine" for you based on which method is called on the DataFrameGroupBy object.
More details and examples of each of these methods are available in the Pandas groupby docs .

'''

import numpy as np

grouped = grocery.groupby('category')

print(grouped.aggregate(['count', 'mean']))

print('\n') #===================================================================================

print(grouped.transform(lambda x: x - x.mean()))

print('\n') #===================================================================================

print(grouped.filter(lambda x: len(x) > 2))

print('\n') #===================================================================================

'''

In the above examples, the index of the new DataFrame is updated according to the method applied.
This is logical behavior, but it's sometimes helpful to be able to treat the grouped index as a regular column.
One situation where this is particularly common is when grouping across more than one column.
The result of such an operation is a hierarchical index or MultiIndex.
When dealing with indexes gets complicated, a good method to keep in mind is .reset_index(),
which assigns the DataFrame's index to the default range of integers and takes whatever had been in the index and puts it in new column(s).

'''

'''

Perform the following operations using split-apply-combine.

Remove all items in categories where the mean price in that category is less than $3.00.
Find the maximum values in each category for all features. (What does Pandas take to be the maximum value of the 'item' column?)
If the maximum price in a category is more than $3.00, reduce all prices in that category by 10%. Return a Series of the new price column.

'''

import pandas as pd
import numpy as np

grocery = pd.DataFrame({'category':['produce', 'produce', 'meat', 'meat', 'meat', 'cheese', 'cheese'],
                        'item':['celery', 'apple', 'ham', 'turkey',  'lamb', 'cheddar', 'brie'],
                        'price':[.99, .49, 1.89, 4.34, 9.50, 6.25, 8.0]})


grouped_grocery = grocery.groupby('category')

one_mean = grouped_grocery.filter(lambda x: x.mean() > 3.00)

two_max = grouped_grocery.max()

three_round = grouped_grocery['price'].apply(lambda x: x - (x*.1) if x.max() > 3.00 else x)

print(one_mean)

print('\n')

print(two_max)

print('\n')

print(three_round)

print('\n')

print(grouped.aggregate(max))