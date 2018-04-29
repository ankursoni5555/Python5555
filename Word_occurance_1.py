# Method to find occurance of all words in a file
# Method 1

from collections import Counter
import re
import string

frequency = {}
document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
print(text_string)

# findall will find all the words matching the criteria mentioned inside, [a-z] = all the words including any letters from
# a to z. {1,15} it defines the range of word, length of word. \b is for the whole word.

match_pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)

d = Counter(match_pattern) # Counter gives the dictionary's key value pair of the words and its value (occurance).

# iterating over dictionary
for key,value in d.items(): # or # for key in d:
    print(key, ':', value)       #     print(key,':',d[key])
