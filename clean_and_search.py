import re
import nltk
import pandas as pd
from cleantext import clean
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from dataset_cleaning.py import dataset_cleaning()
from query_cleaning.py import query_cleaning()


# read from plot_summaries.txt and convert it to csv file
df = pd.read_csv('/put plot_summaries.txt directory address here', delimiter='\t', names=['id', 'overview'])
data = df.to_csv('plot.csv', index=False)

# cleans movie plots and create a new csv file contains cleaned data
input_cleaning(data)

# cleans input term and search for it in 'cleaned_data' column of cleaned_data_file and 
# returns id movies which contain that term
cleaned_data_file = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/plot_cleaned.csv',encoding='utf-8')
query_cleaning(cleaned_data_file, input_term)




