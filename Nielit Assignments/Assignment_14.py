# Ans 1
'''
Answer 1: c. It does not have graphical capabilities.

Answer 2: d. Dataframe allows accessing values as index in loc( ).

Answer 3: a. Series can be created from dataframe.

Answer 4: c. Dataframe cannot be created from dictionary of series.

Answer 5: c. df.iloc[ ] allows accessing rows based on Boolean index only.
'''

# Ans 2
'''
    X   Y   Z
0  78  84  86
1  85  94  97
2  96  89  96
3  80  83  72
4  86  86  83
'''

# Ans 3:
'''
Answer 1:
import pandas as pd

data1 = {
    'month_number': [1, 2, 3, 4, 5, 6],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890],
    'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890],
    'moisturizer': [1500, 1200, 1340, 1130, 1740, 1555]
}

df1 = pd.DataFrame(data1)
print(df1)

Answer 2:
df1['Total_Sales'] = df1.sum(axis=1) - df1['month_number']  # Subtracting month_number as it's not a sales column
print(df1)

Answer 3:
data2 = {
    'month_number': [7, 8, 9, 10, 11],
    'facecream': [2980, 3700, 3540, 1990, 2340],
    'facewash': [1120, 1400, 1780, 1890, 2100],
    'toothpaste': [4780, 5860, 6100, 8300, 7300],
    'bathingsoap': [8980, 9960, 8100, 10300, 13300],
    'shampoo': [1780, 2860, 2100, 2300, 2400],
    'moisturizer': [1120, 1400, 1780, 2300, 2100]
}

df2 = pd.DataFrame(data2)
print(df2)

Answer 4:
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)

Answer 5:
print(df_combined[df_combined['month_number'].isin([7, 8])])

Answer 6:
print(df_combined[df_combined['month_number'].isin([7, 8])])

Answer 7:
print(df_combined[df_combined['month_number'].isin([7, 8])])

'''

# Ans 4
'''
Answer 1:
import pandas as pd

data = {
    'Name': ['Ajay', 'Vijay', 'Sanjay', 'Ajit', 'Vikas', 'Vipul', 'Rakesh'],
    'Jan': [10, 13, 17, 45, 22, 12, 31],
    'Feb': [21, 17, 15, 21, 56, 17, 23],
    'Mar': [23, 12, 16, 7, 76, 22, 27],
    'Apr': [31, 29, 13, 34, 34, 36, 41],
    'May': [7, 14, 18, 22, 22, 31, 32],
    'Jun': [22, 16, 10, 34, 16, 23, 22]
}

df = pd.DataFrame(data)
df.set_index('Name', inplace=True)

total_sales = df.sum(axis=1)
print(total_sales)

Answer 2: 
max_sales = df.max(axis=1)
print(max_sales)

Answer 3: 
vikas_sales = df.loc['Vikas']
print(vikas_sales)

Answer 4: 
apr_sales = df['Apr']
print(apr_sales)

Answer 5: 
feb_jun_sales = df[['Feb', 'Jun']]
print(feb_jun_sales)

Answer 6: 
ajit_sales = df.loc['Ajit', ['Apr', 'May', 'Jun']]
print(ajit_sales)

Answer 7: 
avg_sales = df.mean(axis=1)
print(avg_sales)

Answer 8: 
avg_sales = df.mean(axis=1)
print(avg_sales)

Answer 9: 
min_month_sales = df.min(axis=0)
print(min_month_sales)

Answer 10: 
min_month_sales = df.min(axis=0)
print(min_month_sales)

Answer 11: 
median_month_sales = df.median(axis=0)
print(median_month_sales)

'''