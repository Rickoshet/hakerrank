N, K, Q = list(map(int, input().strip().split()))
A = list(map(int, input().strip().split()))
result = []
for q in range(Q):
    q = int(input())
    result.append(A[q-K % N])
for i in result:
    print(i)
