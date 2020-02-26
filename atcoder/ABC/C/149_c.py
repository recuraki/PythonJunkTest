
def prime_list_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
def prime_list_eratosthenes_from(n_from, n_to):
    from bisect import bisect_left
    data = prime_list_eratosthenes(n_to)
    i = bisect_left(data, n_from)
    return data[i:]
x = int(input())
d = prime_list_eratosthenes_from(x, 1000000)
print(d[0])
