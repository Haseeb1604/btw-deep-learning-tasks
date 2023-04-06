import seaborn as sns

df = sns.load_dataset('titanic')

print(df.isnull().sum())
# Output
# survived      0
# pclass        0
# sex           0
# age         177
# sibsp         0
# parch         0
# fare          0
# embarked      2
# class         0
# who           0
# adult_male    0
# deck        688
# embark_town   2
# alive         0
# alone         0
# dtype: int64

# there are missing values in the columns age, embarked, deck, and embark_town.

# Filling and Replacing Values:
# Filling missing values using fillna() method.

df['age'].fillna(df['age'].mean(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df.drop(['deck', 'embark_town'], axis=1, inplace=True)

# Checking for Duplicates and Removing if any
print(df.duplicated().sum()) # Output: 0

# Detecting and Removing Outliers
print(df.describe())

# Output
#          survived      pclass         age       sibsp       parch        fare
# count  891.000000  891.000000  891.000000  891.000000  891.000000  891.000000
# mean     0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std      0.486592    0.836071   13.002015    1.102743    0.806057   49.693429
# min      0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%      0.000000    2.000000   22.000000    0.000000    0.000000    7.910400
# 50%      0.000000    3.000000   29.699118    0.000000    0.000000   14.454200
# 75%      1.000000    3.000000   35.000000    1.000000    0.000000   31.000000
# max      1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

# Using boxplot() method to visualize the distribution of the numerical columns in the dataset.

import matplotlib.pyplot as plt

df.boxplot()
plt.show()

# There are a few outliers in the fare column Removing it using IQR Method
# Calculate IQR
Q1 = df['fare'].quantile(0.25)
Q3 = df['fare'].quantile(0.75)
IQR = Q3 - Q1

# Calculate upper and lower bounds
upper_bound = Q3 + 1.5 * IQR
lower_bound = Q1 - 1.5 * IQR

# Remove outliers
df = df[(df['fare'] >= lower_bound) & (df['fare'] <= upper_bound)]
