def inverted_index(cleaned_data_file, ):
  inv_idx_dict = {}
  for i in range(0, len(clened_data_file)):
    for word in cleaned_data_file.loc[i, "cleaned_data"].split():
      if word not in inv_idx_dict.keys():
        inv_idx_dict[word] = [cleaned_data_file.loc[i, "id"]]
      else:
        inv_idx_dict[word].append(cleaned_data_file.loc[i, "id"])
  for each_key, value in inv_idx_dict.items():
     inv_idx_dict[each_key] = list(set(value))
  return inv_idx_dict
