def lcm(n,m):
    if n>m:
        l=n
        den=m
    else:
        l=m
        den=n
    rem=l%den
    while rem!=0:
        l=den
        den=rem
    gcd=den
    


l=[1,2,3,4,5,6,7,8,9]
num1=l[0]
num2=l[1]
lcm=0
for i in range(2,len(l)):
    lcm=lcm(lcm.l[i])

print(lcm)