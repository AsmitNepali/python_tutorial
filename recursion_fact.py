i = 5
def re_fact(n):

    if n==0:
        return 1    
    return n * re_fact(n-1)
resutl = re_fact(5)

print(resutl)

