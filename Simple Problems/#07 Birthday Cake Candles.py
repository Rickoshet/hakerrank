n = input()
arr = input().split()
Max, count = 0, 0
for x in arr:
    x = int(x)
    if x > Max:
        Max = x
        count = 1
    elif x == Max:
        count += 1
print(count)
