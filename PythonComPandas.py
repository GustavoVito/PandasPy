import pandas as pd

df = pd.read_csv('tmdb_5000_credits.csv')

print(df.head())

print(df[['title', 'cast']])

for index, row in df.iterrows():
    title = row['title']
    cast = row['cast']
    actors = cast.split(', ')
    for actor in actors:
        print(f'{title} | {actor}')