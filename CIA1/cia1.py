import numpy as np
import random as rd
 
chars = ['a','c','g','t']
word_len = 16
i=j=1

def word_generator(word_len):
    word = ""
    a = c = g = t = 0
    while len(word) < word_len:
        ch = rd.choice(chars)
        if ch=='a' and a<4:
            word+=ch
            a+=1
        elif ch=='c' and c<4:
            word +=ch
            c+=1
        elif ch=='g' and g < 4:
            word +=ch 
            g+=1
        elif ch == 't' and t < 4:
            word +=ch
            t+=1
    return word

word1 = word_generator(word_len)
word2 = word_generator(word_len)

def recursive_compare(word1,word2,i,j,matrix):
    if i == 0 or j == 0:
        return 0
    if matrix[i][j] != 0:
        return matrix[i][j]
    if word1[i - 1] == word2[j - 1]:
        matrix[i][j] = recursive_compare(word1, word2, i - 1, j - 1, matrix) + 2
    else:
        matrix[i][j] = max(recursive_compare(word1, word2, i - 1, j, matrix), recursive_compare(word1, word2, i, j - 1, matrix), recursive_compare(word1, word2, i - 1, j - 1, matrix)) - 1
    return matrix[i][j]

def compare_strings(string1, string2):
    matrix = np.zeros((len(word1) + 1, len(word2) + 1))
    recursive_compare(string1, string2, len(string1), len(string2), matrix)
    return matrix

results = compare_strings(word1,word2)
print(results)
