import re
import nltk
import pandas as pd
from cleantext import clean
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# read from plot_summaries.txt and convert it to csv file
df = pd.read_csv('/put plot_summaries.txt directory address here', delimiter='\t', names=['id', 'overview'])
data = df.to_csv('plot.csv', index=False)

# iterate over 'overview' column of each row and clean it
ps = PorterStemmer()
cleans_data=[]

 
 # create new csv file which include 'cleaned_data' column
data.to_csv('plot_cleaned.csv', index=False)  


