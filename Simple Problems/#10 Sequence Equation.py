n = int(input().strip())
p = list(map(int, input().strip().split()))
for i in range(1, n+1):
    print(p.index(p.index(i)+1)+1)
