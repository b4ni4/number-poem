from words import d

def parse(n):
    to_word = lambda x: d[int(x)]

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

    for w in arr:
        for k, v in d.items():
            if v == w:
                sum += k
    
    return sum
    
def main():
    n = int(input())

    words = parse(n)
    print(words)

    deparsed = deparse(input().split())
    print(deparsed)
    print(n == deparsed)

if __name__ == '__main__':
    main()
