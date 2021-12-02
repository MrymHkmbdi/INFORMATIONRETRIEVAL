import re
import nltk
import pandas as pd
from cleantext import clean
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from term_cleaning.py import term_cleaning()
from query_cleaning.py import query_cleaning()
from inverted_index.py import inverted_index()
from dataset_cleaning.py import dataset_cleaning()
from print_ten_most_related.py import print_ten_most_related()



# read from plot_summaries.txt and convert it to csv file
df = pd.read_csv('/put plot_summaries.txt directory address here', delimiter='\t', names=['id', 'overview'])
data = df.to_csv('plot.csv', index=False)

# cleans movie plots and create a new csv file contains cleaned data
input_cleaning(data)
cleaned_data_file = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/plot_cleaned.csv',encoding='utf-8')

# cleans input term and search for it in 'cleaned_data' column of cleaned_data_file and 
# returns id movies which contain that term
# input_term must be a word
query_cleaning(cleaned_data_file, input_term)


# calculate inverted_index of the whole document
inverted_index = {}
inverted_index = inverted_index(cleaned_data_file)

# save inverted index to a csv file
pd.DataFrame.from_dict(data=inv_idx_dict, orient='index').to_csv('/directory you want to save inverted-index.csv/inverted-index.csv', header=False)

# cleans query
# query must be a question which must be longer than 4 words after cleaning
cleaned_query = query_cleaning(query)

# calculate cosine similarity of query and document and returns 10 most related plots and their ids as a csv file
cosine_similarity(cleaned_data_file, cleaned_query)

# read csv file that contains 10 most related movies, calculated in line 45  
queriy_and_movies = pd.read_csv("/content/drive/MyDrive/queryandmovies/1.csv")


# print id_plot_dict = {id: overview} of 10 most related movies
print_ten_most_related(queriy_and_movies)



