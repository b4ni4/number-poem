from words import d

to_word = lambda x: d[int(x)]

def parse(n):
    l = len(str(n))

    if l >= 2 and str(n)[-2] == '1':
        yield n % 100
        n //= 100
        n *= 100

    for i in range(l):
        x = n % 10
        n //= 10

        if x:
            yield x * 10 ** i

def main():
    n = int(input())

    res = []
    for i in parse(n):
        res.append(to_word(i))

    print(' '.join(reversed(res)))
    

if __name__ == '__main__':
    main()
