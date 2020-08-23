import random
from words import ddd1, d_new, d_formula
from parser import deparse, get_parsed_string

def is_legit(string):
    words = string.split()
    restart = True
    while restart:
        restart = False
        for i in range(len(words)-1):
            if get_parsed_string(deparse((words[i] + ' '+ words[i+1]).split())) == words[i] + ' ' + words[i+1]:
                words[i] += (' ' + words[i+1])
                words.pop(i+1)
                restart = True
                break
    return words

def get_rhythmic(word):
    sylled_word = ddd1[word]

    if (len(sylled_word) == 1):
        return '1'

    res = ''

    for i in range(len(sylled_word)):
        for char in sylled_word[i]:
            if char == "'":
                res += '1'
                res += (len(sylled_word) - i - 1) * '0'
                return  res
        res += '0'
    return res

def cosntruct_line(formula):
    res = ''

    if formula == '010':
        res += random.choice(d_formula['010'])
        return res + ' '

    if formula == '10':
        res += random.choice(d_formula['10'])
        return res + ' '

    pair = random.choice(list(d_new.items()))
    if pair[1] == formula:
        res += pair[0]
        return res
    elif pair[1] == formula[:len(pair[1])]:
        res += pair[0]
        return res + ' ' + cosntruct_line(formula[len(pair[1]):])
    else:
        return cosntruct_line(formula)

formula = input()
for i in range(100):
    try:
        deg = cosntruct_line(formula)
        print(deg)
        print(is_legit(deg))
        s = ''
        for word in deg:
            s += d_new[word]
        if formula == s:
            print('True')
    except:
        continue

# word = input()
# print(get_rhythmic(word))