def alldig(n):
    n=str(n)
    l=[0]*len(n)
    prime=['2','3','5','7']
    for i in range(len(n)):
        l[i]=n[i]
    for i in range(len(n)):
        if l[i] not in prime:
            return False
    return int(''.join(l))

    
def isprime(N):
    while(N!=0):
        res=alldig(N)
        if res:
            return res
        else:
            N-=1
    return 'No prime'

print(isprime(10))
