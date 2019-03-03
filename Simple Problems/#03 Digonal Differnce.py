arr = []
n = int(input())
sum1 = 0
sum2 = 0
q = n-1

for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    sum1 = sum1+ arr[i][i]
    sum2 = sum2 + arr[i][q]
    q -= 1
print(abs(sum1-sum2))
