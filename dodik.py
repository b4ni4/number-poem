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

poems_nums = []
poems_text = []
formula = input()

arr_num = []
arr_text = []
mas_num = []
mas_text = []

for i in range(100):
    try:
        deg = is_legit(cosntruct_line(formula))
        for num in deg:
            mas_num.append(deparse(num.split(' ')))
            mas_text.append(num)
        arr_num.append(mas_num)
        arr_text.append(mas_text)
        mas_num = []
        mas_text = []
        if len(arr_num) == 4:
            poems_nums.append(arr_num)
            arr_num = []
            poems_text.append(arr_text)
            arr_text = []
    except:
        continue
for poem in poems_nums:
    print('\n')
    for string in poem:
        s = ''
        for i in range(len(string)):
            s += (str(string[i]) + ' ')
        print(s)

for poem in poems_text:
    print('\n')
    for string in poem:
        s = ''
        for i in range(len(string)):
            s += (string[i] + ' ')
        print(s)
# word = input()
# print(get_rhythmic(word))