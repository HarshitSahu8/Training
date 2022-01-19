num=int(input())

lst_num=num%10
n=num
leng=0
while (n!=0):
    n=int(n/10)
    leng+=1
leng-=1
#print(leng-1)
#obtain 10000 the 12345/10000
ze=(10**leng)
#print(ze)
fstD=int(num/ze)
#print(fstD)
snum=lst_num
snum*=int(10**leng)
snum+=num%int(10**leng)
snum-=lst_num
snum+=fstD
print(snum)


