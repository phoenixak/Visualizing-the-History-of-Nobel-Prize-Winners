# Importing required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Loading the Nobel Prize data
nobel_data = pd.read_csv('dataset\\nobel.csv')

# Displaying the first few rows of the data to understand its structure
print(nobel_data.head())
print(nobel_data.columns)

# Analyzing the most common gender and birth country
top_gender = nobel_data['sex'].mode()[0]
top_country = nobel_data['birth_country'].mode()[0]
print(f"The most commonly awarded gender is: {top_gender}")
print(f"The most commonly awarded birth country is: {top_country}")

# Preparing data for US-born winners analysis
nobel_data['US_born'] = nobel_data['birth_country'] == 'United States of America'
nobel_data['year'] = pd.to_datetime(nobel_data['year'], format='%Y', errors='coerce')
nobel_data['decade'] = nobel_data['year'].dt.year // 10 * 10

# Calculating the ratio of US-born winners for each decade
us_born_ratio = nobel_data.groupby('decade')['US_born'].mean()
max_decade_usa = us_born_ratio.idxmax()
print(f"The decade with the highest ratio of US-born Nobel Prize winners is: {max_decade_usa}")

# Analyzing the proportion of female laureates for each decade and category
female_proportion = nobel_data.groupby(['decade', 'category'])['sex'].apply(lambda x: (x == 'Female').sum() / len(x))
max_female_decade_category = female_proportion.idxmax()
max_female_dict = {max_female_decade_category[0]: max_female_decade_category[1]}
print(f"The decade and category with the highest proportion of female laureates is: {max_female_dict}")

# Identifying the first woman to receive a Nobel Prize
first_woman = nobel_data[nobel_data['sex'] == 'Female'].sort_values(by='year')
first_woman_name = first_woman.iloc[0]['full_name']
first_woman_category = first_woman.iloc[0]['category']
print(f"The first woman to receive a Nobel Prize was: {first_woman_name}")
print(f"She received the prize in the category: {first_woman_category}")

# Identifying individuals or organizations who have won more than one Nobel Prize
prize_counts = nobel_data['full_name'].value_counts()
repeat_winners = prize_counts[prize_counts > 1]
repeat_list = repeat_winners.index.tolist()
print(f"Individuals or organizations who have won more than one Nobel Prize are: {repeat_list}")
