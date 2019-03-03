def dynamicArray(n, queries):
    lastNumber = 0
    seqList=[];
    for i in range(n):
        seqList.append([])
    res = [];
    for k, x, y in queries:
        index = (x^lastNumber)%n
        if k==1:
            seqList[index].append(y)
        else:
            size = len(seqList[index])
            lastNumber = seqList[index][y%size]
            res.append(lastNumber)
    return res

n, q = list(map(int, input().strip().split()))
queries = []
for i in range(q):
    queries.append(list(map(int, input().rstrip().split())))

print('\n'.join(map(str, dynamicArray(n, queries))))
print('\n')
