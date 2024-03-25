from multiprocessing import Pool
multi = 10

N = 10**4
mod = 10**9 + 7

def f(x):
    data = [x] * N
    for i in range(N):
        for j in range(N):
            for k in range(N):
                data[i] += data[j] + data[k]
                data[i] %= mod
    return sum(data) % mod

if __name__ == '__main__':
    with Pool(multi) as p:
        print(p.map(f, list(range(multi))))
