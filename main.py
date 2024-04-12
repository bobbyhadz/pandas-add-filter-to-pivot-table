# How to add a Filter to Pivot Table in Pandas

import pandas as pd

df = pd.DataFrame({
    'id': [1, 1, 2, 2, 3, 3],
    'name': ['Alice', 'Alice', 'Bobby', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 2, 2, 3, 3, 8],
})


table = df[df['id'] > 1].pivot_table(
    index='id',
    columns=['name'],
    values='experience',
    aggfunc='mean'
)

# name  Bobby  Carl  Dan
# id
# 2       2.5   NaN  NaN
# 3       NaN   3.0  8.0
print(table)