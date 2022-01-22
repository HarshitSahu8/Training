def marge(arr1,arr2,size1,size2):
    arr3=[0]*(size1+size2)
    i=0
    j=0
    k=0
    while i<size1 and j<size2:
        if arr1[i]<arr2[j]:
            arr3[k]=arr1[i]
            k+=1
            i+=1
        else:
            arr3[k]=arr2[j]
            k+=1
            j+=1
    while i<size1:
        arr3[k]=arr1[i]
        k+=1
        i+=1
    while j<size2:
        arr3[k]=arr2[j]
        k+=1
        j+=1
    return arr3
            
    
m=int(input('enter m: '))
n=int(input('enter n: '))
num1=[0]*m
num2=[0]*n
print('enter value of num1')
for i in range(m):
    num1[i]=int(input())
print('enter value of num2')
for j in range(n):
    num2[j]=int(input())
res=marge(num1,num2,m,n)
if (m+n)%2==0:
    ptr=(m+n)//2
    s=res[ptr-1]+res[ptr]
    s=s//2
    print(s)
else:
    ptr=int((m+n)/2)
    print(res[ptr])
    