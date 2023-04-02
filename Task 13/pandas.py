# Pandas, popular library for data manipulation and analysis. It provides two main data structures for handling tabular data: Series and DataFrame.

# A Series is a one-dimensional array-like object that can hold any data type (e.g. integers, floating-point numbers, strings, etc.) and an associated array of data labels, called an index.

# A DataFrame is a two-dimensional tabular data structure, consisting of rows and columns, similar to a spreadsheet or SQL table. Each column in a DataFrame can have a different data type, and the entire DataFrame can be thought of as a collection of Series.

import pandas as pd

# create a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# print the Series
print(s)

# Output
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

# create a DataFrame from a dictionary of lists
data = {'name': ['Haseeb', 'Hassaan', 'Zakarya', 'Talal'],
        'age': [22, 21, 23, 19]}

df = pd.DataFrame(data)

# print the DataFrame
print(df)

# Output
#        name  age 
# 0    Haseeb   22 
# 1   Hassaan   21 
# 2   Zakarya   23 
# 3     Talal   19


# Accessing and slicing data in a Series
# access the first element of the Series
print(s[0])  

# Output: 1.0

# slice the Series to get elements from index 2 to 4
print(s[2:5])  
# Output: 
# 2    5.0
# 3    NaN
# 4    6.0
# dtype: float64

# Accessing and slicing data in a DataFrame
# access the 'name' column of the DataFrame
print(df['name'])  
# Output:
# 0     Haseeb
# 1    Hassaan
# 2    Zakarya
# 3      Talal
# Name: name, dtype: object

print(df[1:3])  

# Output:
#        name  age
# 1   Hassaan   21
# 2   Zakarya   23


# Adding a new column to a DataFrame
# add a new column 'gender' to the DataFrame
df['gender'] = ['M', 'M', 'M', 'M']

print(df)  

# Output:
#       name  age gender
# 0    Haseeb   22      M
# 1   Hassaan   21      M
# 2   Zakarya   23      M
# 3     Talal   19      M

# Filtering data based on a condition
# filter the DataFrame to get rows where age is greater than 21
filtered_df = df[df['age'] > 21]

print(filtered_df)  

# Output:
#       name  age gender
# 0    Haseeb   22      M
# 2   Zakarya   23      M

# Applying a function to a column in a DataFrame
# apply a function to the 'age' column to calculate age in months
def calculate_age_in_months(age):
    return age * 12

df['age_in_months'] = df['age'].apply(calculate_age_in_months)

print(df)  

# Output:
#       name  age gender  age_in_months
# 0    Haseeb   22      M            264
# 1   Hassaan   21      M            252
# 2   Zakarya   23      M            276
# 3     Talal   19      M            228

# add a new row to the DataFrame using .append method
new_row = {'name': 'Fatima', 'age': 22, 'gender': 'F'}
df = df.append(new_row, ignore_index=True)

# add multiple rows to the DataFrame using .append method
new_rows = [{'name': 'Hafsa', 'age': 26, 'gender': 'F'},
            {'name': 'Seher', 'age': 24, 'gender': 'F'}]
df = df.append(new_rows, ignore_index=True)

print(df)

#       name  age gender  age_in_months
# 0   Haseeb   22      M          264.0
# 1  Hassaan   21      M          252.0
# 2  Zakarya   23      M          276.0
# 3    Talal   19      M          228.0
# 4   Fatima   22      F            NaN
# 5    Hafsa   26      F            NaN
# 6    Seher   24      F            NaN
# 7   Fatima   22      F            NaN
# 8    Hafsa   26      F            NaN
# 9    Seher   24      F            NaN


# add a new column to the DataFrame using .insert method
tech_stack = ['NLP', 'Missing', 'Flutter', 'Web', 'AI', 'Web', 'Image Processing']
df.insert(3, 'Tech Stack', tech_stack)
print(df)

#       name  age gender        Tech Stack  age_in_months
# 0   Haseeb   22      M               NLP          264.0
# 1  Hassaan   21      M           Missing          252.0
# 2  Zakarya   23      M           Flutter          276.0
# 3    Talal   19      M               Web          228.0
# 4   Fatima   22      F                AI            NaN
# 5    Hafsa   26      F               Web            NaN
# 6    Seher   24      F  Image Processing            NaN


# Grouping data by gender and calculating the mean age
grouped = df.groupby('gender')['age'].mean()

print(grouped)

# Output
# gender
# F    24.00
# M    21.25
# Name: age, dtype: float64

# Filtering data based on multiple conditions
filtered_df = df[(df['gender'] == 'F') & (df['age'] > 22)]

print(filtered_df)
#     name  age gender        Tech Stack  age_in_months
# 5  Hafsa   26      F               Web            NaN
# 6  Seher   24      F  Image Processing            NaN


sorted_df = df.sort_values(by='age', ascending=False)

print(sorted_df)

#       name  age gender        Tech Stack  age_in_months
# 5    Hafsa   26      F               Web            NaN
# 6    Seher   24      F  Image Processing            NaN
# 2  Zakarya   23      M           Flutter          276.0
# 0   Haseeb   22      M               NLP          264.0
# 4   Fatima   22      F                AI            NaN
# 1  Hassaan   21      M           Missing          252.0
# 3    Talal   19      M               Web          228.0

df = df.drop('age_in_months', axis=1)

df = df.rename(columns={'name': 'full_name', 'Tech Stack': 'tech'})

print(df)

#   full_name  age gender              tech
# 0    Haseeb   22      M               NLP
# 1   Hassaan   21      M           Missing
# 2   Zakarya   23      M           Flutter
# 3     Talal   19      M               Web
# 4    Fatima   22      F                AI
# 5     Hafsa   26      F               Web
# 6     Seher   24      F  Image Processing

grouped = df.groupby('gender')['age'].agg(['mean', 'median', 'min', 'max'])

print(grouped)

#          mean  median  min  max
# gender                         
# F       24.00    24.0   22   26
# M       21.25    21.5   19   23


# iloc: used to select rows and columns by integer position. It stands for "integer location".
# loc:  used to select rows and columns by label. It stands for "location".

# select rows using iloc
print(df.iloc[0])  # select first row
# full_name    Haseeb
# age              22
# gender            M
# tech            NLP
# Name: 0, dtype: object

print(df.iloc[1:4])  # select rows 1 to 3
#   full_name  age gender     tech
# 1   Hassaan   21      M  Missing
# 2   Zakarya   23      M  Flutter
# 3     Talal   19      M      Web

# select rows using loc
print(df.loc[0])  # select first row
# full_name    Haseeb
# age              22
# gender            M
# tech            NLP
# Name: 0, dtype: object

print(df.loc[1:4])  # select rows 1 to 3
#   full_name  age gender     tech
# 1   Hassaan   21      M  Missing
# 2   Zakarya   23      M  Flutter
# 3     Talal   19      M      Web

print(df.loc[df['gender'] == 'F'])  # select rows where gender is 'F'
#   full_name  age gender              tech
# 4    Fatima   22      F                AI
# 5     Hafsa   26      F               Web
# 6     Seher   24      F  Image Processing
