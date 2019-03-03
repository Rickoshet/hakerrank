a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
Alice = 0
Bob = 0
for i in range(len(a)):
    if a[i]>b[i]:
        Alice+=1
    elif b[i]>a[i]:
        Bob+=1
    else:
        pass
print(Alice,Bob)
