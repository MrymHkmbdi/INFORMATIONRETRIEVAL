def cosine_similarity(cleaned_data_file, cleaned_query):
  tfidf_score = TfidfVectorizer()
  movie_tfidf = tfidf_score.fit_transform(cleaned_data_file['cleaned_data'].to_list())
  query_tfidf = tfidf_score.transform([cleaned_query])
  similarity = cosine_similarity(query_tfidf, movie_tfidf)
  for i, row in enumerate(similarity):
      cleaned_data_file.loc[(-row).argsort()[:10]].to_csv("queryandmovies/{}.csv".format(query),index=False)
