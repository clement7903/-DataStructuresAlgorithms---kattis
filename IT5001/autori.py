name = input()

def shorten_iteration(name):
  output = ''
  for chr in name:
    if chr.isupper():
      output += chr
  print(output)

shorten_iteration('Knuth-Morris-Pratt')