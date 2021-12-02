def term_cleaning(cleaned_data_file, input_term):
  cleaned_data_file = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/plot_cleaned.csv',encoding='utf-8')
  ps = PorterStemmer()
  cleans_data=[]
  terms = []
  counter = 0
  clean_data=clean('{}'.format(input_term),
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
  ans = ps.stem(clean_data)
  for i in range(0,len(cleaned_data_file)):
    for word in cleaned_data_file.loc[i, "cleaned_data"].split():
      if ans in word:
        terms.append(cleaned_data_file.loc[i, "id"])
      else:
        continue
  mylist = list(dict.fromkeys(terms))
print('Term {} repeated {} times in films listed below: '.format(input_term, len(mylist)))
