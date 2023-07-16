import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

list_for_vector = list(set(lst))

for i, o in data.iterrows():
    data.loc[i, 'one_hot'] = list_for_vector.index(o['whoAmI'])

data['one_hot'] = data['one_hot'].astype('int')
# data.drop(['whoAmI'], axis = 1, inplace = True)

data