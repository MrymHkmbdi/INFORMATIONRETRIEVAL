def print_ten_most_related(queriy_and_movies, ):
  ids = []
  overview = []
  for i in range(len(queriy_and_movies)):
    overview.append(queriy_and_movies.loc[i, 'overview'])
    ids.append(queriy_and_movies.loc[i, 'id'])
  zip_it = zip(ids, overview)
  id_plot_dict = dict(zip_it)
  for k,v in id_plot_dict.items():
    print('{}: {}\n'.format(k,v))
