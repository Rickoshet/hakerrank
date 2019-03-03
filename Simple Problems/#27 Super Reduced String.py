s = input()

def super_reduced_string(s):
    res = [] # stack
    for c in s:
        if res and res[len(res)-1] == c: # peek what's on top
            res.pop()
        else:
            res.append(c)    
    res = ''.join(res)
    return res or 'Empty String'
    
print(super_reduced_string(s))
