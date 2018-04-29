import re
import string

frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{5,15}\b', text_string)
print(match_pattern)

for word in match_pattern:
      count = frequency.get(word, 0)
      frequency[word] = count + 1

print(frequency)
#frequency_list = frequency.keys()


for words in frequency:
      print(words, frequency[words])

