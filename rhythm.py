from words import d4, d5

def get_rhythmic(word):
    sylled_arr = d4[word]
    word_w_stress = d5[word]
    index_stressed = -1
    for i in range(len(word_w_stress)):
        if word_w_stress[i] == "'":
            index_stressed = i - 1
            break
    if index_stressed == -1:
        return '1'
    sum = -1
    syll_stressed = -1
    for i in range(len(sylled_arr)):
        sum += len(sylled_arr[i])
        if sum >= index_stressed:
            syll_stressed = i
            break
    res = ''
    for i in range(len(sylled_arr)):
        if i == syll_stressed:
            res += '1'
        else:
            res += '0'
    return res

word = input()
print(get_rhythmic(word))


