def query_cleaning(query):
  ps = PorterStemmer()
  cleans_data=[]
  clean_data=clean('{}'.format(query),
          fix_unicode=True,               # fix various unicode errors
          to_ascii=True,                  # transliterate to closest ASCII representation
          lower=True,                     # lowercase text
          no_line_breaks=True,           # fully strip line breaks as opposed to only normalizing them
          no_urls=True,                  # replace all URLs with a special token
          no_emails=True,                # replace all email addresses with a special token
          no_phone_numbers=True,         # replace all phone numbers with a special token
          no_numbers=False,               # replace all numbers with a special token
          no_digits=False,                # replace all digits with a special token
          no_currency_symbols=True,      # replace all currency symbols with a special token
          no_punct=True,                 # remove punctuations
          replace_with_punct="",          # instead of removing punctuations you may replace them
          replace_with_url="<URL>",
          replace_with_email="<EMAIL>",
          replace_with_phone_number="<PHONE>",
          replace_with_number="<NUMBER>",
          replace_with_digit="0",
          replace_with_currency_symbol="<CUR>",
          lang="en"                       # set to 'de' for German special handling
    )
  nltk_english_stopwords = stopwords.words('english')
  cleaned_query = ""
  words=re.sub("[^\w]", " ", clean_data).split()
  for w in words:
    if w not in nltk_english_stopwords:
      cleaned_query = cleaned_query + " "+ ps.stem(w)
  return cleaned_query
