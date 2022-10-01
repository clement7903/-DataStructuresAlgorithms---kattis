def remove_adj_repeated_letters(stringofwords):
  if not stringofwords:
    return ''
  if len(stringofwords) == 1:
    return stringofwords
  if stringofwords[0] == stringofwords[1]:
    return remove_adj_repeated_letters(stringofwords[1:])
  return stringofwords[0] + remove_adj_repeated_letters(stringofwords[1:])

def remove_aeiou(stringofwords):
  lst = ['a', 'e', 'i', 'o', 'u']
  words = stringofwords.split()
  output = []
  for word in words:
    if len(word) == 1:
      output.append(word)
    else:
      final_word = word[0]
      word_mid = word[1:-1]
      word_end = word[-1]
      for char in word_mid:
        if char not in lst:
          final_word += char
      final_word += word_end
      output.append(final_word) 
  return ' '.join(output)

num_words = input()
stringofwords = str(input())

print(remove_aeiou(remove_adj_repeated_letters(stringofwords)))