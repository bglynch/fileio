# Getting data from files--------------------------------------------------------------------
#readlines method--------------------------------------------------
# f = open("data.txt", "r")   # r = read mode, f = file handle
# lines = f.readlines()       # create a copy of the file in memory
# f.close()                   # close the file
# print(lines)


#split() method--------------------------------------------------

# f = open('data.txt', 'r')   
# lines = f.read().split('\n')
# f.close()
# print(lines)

# getting 10 most common words from book-------------------------
import re # "imports pythons regular expression library"
import collections  # imports collections library

bookText = open("1155-0.txt").read().lower()
words = re.findall("\w+", bookText)     # \w = not whitespace  + = more than one

long_words = []
for word in words:
    if len(word) > 16:
        long_words.append(word)
    

most_common = collections.Counter(long_words).most_common(20)
print(most_common)
