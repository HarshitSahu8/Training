size=int(input())
arr=[0]*size
k=int(input())
for i in range(size):
    arr[i]=int(input())
st=0
ed=k
mx=0
while(ed<=size):
    mx=0
    for i in range(st,ed):
        if mx<arr[i]:
            mx=arr[i]
    print(mx)
    st+=1
    ed+=1
    
