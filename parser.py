from words import d
from russtress import Accent

def get_parsed_string(n):
    words = parse(n)

    if n >= 1000:
        res = declination(words)
        return res.rstrip()
    else:
        res = ' '.join(words)
        return res

def declination(words):
    res = ''
    if isinstance(words[0], list):
        for i in range(len(words)):
            k = 10 ** (3 * (len(words) - i - 1))
            if k == 1 and words[i][-1] != 'ноль':
                res += ' '.join(words[i])
                continue

            declination_flag = 0
            if words[i][-1] == 'ноль':
                continue
            if words[i][-1] == d[1][declination_flag]:
                if k == 1000:
                    declination_flag = 1
                    words[i][-1] = d[1][declination_flag]
                words[i].append(d[k][0] + ' ')
                res += ' '.join(words[i])
                continue

            elif words[i][-1] == d[2][declination_flag]:
                if k == 1000:
                    declination_flag = 1
                    words[i][-1] = d[2][declination_flag]
                words[i].append(d[k][1] + ' ')
                res += ' '.join(words[i])
                continue
            else:
                if words[i][-1] == d[3] or words[i][-1] == d[4]:
                    words[i].append(d[k][1] + ' ')
                    res += ' '.join(words[i])
                else:
                    words[i].append(d[k][2] + ' ')
                    res += ' '.join(words[i])
        return res

def parse(n):
    to_word = lambda x: d[int(x)] if isinstance(d[int(x)], str) else d[int(x)][0]

    if n >= 1000:
        millenium_split = []
        k = n
        while k >= 1000:
            q = k % 1000
            millenium_split.append(q)
            k //= 1000
        millenium_split.append(k)

        millenium_split = list(reversed(millenium_split))

        res_m = []
        for split in millenium_split:
            res_m.append(parse(int(split)))
        return res_m

    def parse_nums(n):
        l = len(str(n))


        if int(n) == 0:
            yield 0
            return

        if l >= 2 and str(n)[-2] == '1':
            yield n % 100
            n //= 100
            n *= 100

        for i in range(l):
            x = n % 10
            n //= 10

            if x:
                yield x * 10 ** i

    res = []
    for i in parse_nums(n):
        res.append(to_word(i))

    return list(reversed(res))

def deparse(arr):
    sum = 0


    # for w in arr:
    #     for k, v in d.items():
    #         if v == w:
    #             sum += k
    cur = 0
    for w in arr:
        for k, v in d.items():
            if isinstance(v, list):
                if len(v) == 3 and w in v:
                    cur *= k
                    sum += cur
                    cur = 0
                elif w in v:
                    cur += k
            else:
                if v == w:
                    cur += k

    return sum + cur


def accent(text):
    accent = Accent()
    return accent.put_stress(text)
    
def main():
    n = int(input())
    print(get_parsed_string(n))
    string = input()
    deparsed = deparse(string.split(' '))
    print(deparsed)
    # if deparsed == n:
    #     print('True')
    # else:
    #     print('False')

if __name__ == '__main__':
    main()
