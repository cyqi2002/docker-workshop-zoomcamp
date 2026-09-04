import sys
sys.argv #sys.argv[0] is the program file name, sys.argv[1] is the first argument, and so on

import pandas as pd

print('arguments', sys.argv)

month=int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())


df.to_parquet(f'output_{month}.parquet')
print(f'hello pipeline, month ={month}')