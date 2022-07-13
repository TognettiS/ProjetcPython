import string
import re

x = input('Digite as palavras separando por espaço: ')
print("\n")
y = x.split()

for i in range(len(y)):
    y[i] = y[i].capitalize()

a = max(y, key = len).translate(str.maketrans("","", string.punctuation))
print (a)
z = ''
z = z.join(y).capitalize().translate(str.maketrans("","", string.punctuation))
