n = int(input())
arr = list(map(int, input().strip().split()))

positive = sum(x > 0 for x in arr) / n
negative = sum(x < 0 for x in arr) / n
zero = sum(x == 0 for x in arr) / n
    
print(positive, negative, zero, sep="\n")
