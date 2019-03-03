from itertools import product

def spent(K, D, b):
    return max((k+d if k+d<=b else -1 for k,d in product(K,D)))

b, n, m, = list(map(int, input().strip().split()))
K = list(map(int, input().strip().split()))
D = list(map(int, input().strip().split()))

print(spent(K, D, s))
