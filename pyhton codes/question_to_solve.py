
def count_first_letter(names):
    first_letter_list = []
    value_list = []
    for key, value in names.items():
        first_letter_list.append(key[0])
        value_list.append(value)
    print(value_list)

    common_index_val_list = []
    uniq_key_list = []
    for first_letter in first_letter_list:
        if not(first_letter in uniq_key_list):
            uniq_key_list.append(first_letter)
            common_index_val_list.append([i for i in range(len(first_letter_list)) if first_letter_list[i] == first_letter])
    #return common_index_val_list
    words_merged = {}
    for indexes in common_index_val_list:
        sum = 0
        for pos in indexes:
            sum += len(value_list[pos])
        words_merged[uniq_key_list[common_index_val_list.index(indexes)]] = sum
    return words_merged

# Another short method
"""def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters"""











print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
