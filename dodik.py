import random
from words import ddd1, d_new, d_formula
d_avai = {
    'a': '1',
    'b': '10',
    'c': '01',
    'd': '100',
    'e': '010',
    'f': '0100',
    'g': '001',
    'h': '0010'
}

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
for i in range(10):
    try:
        deg = cosntruct_line(formula)
        print(deg)
        s = ''
        for char in deg:
            s += d_avai[char]
        if formula == s:
            print('True')
    except:
        continue

# word = input()
# print(get_rhythmic(word))