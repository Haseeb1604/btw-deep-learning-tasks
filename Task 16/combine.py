import pandas as pd
import numpy as np

train_df = pd.read_csv('train_df.csv')
test_df = pd.read_csv('test_df.csv')

# combining the datasets vertically
df = pd.concat([train_df, test_df])

print(df)


ratings = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6],
    'movie_id': ['A', 'B', 'C', 'D', 'E', "F"],
    'rating': [3, 4, 5, 2, 1, 4]
})

ratings_matrix = np.reshape(ratings['rating'].values, (6, 1))

print(ratings_matrix)