arr=[100,200,500,2000]
freq=[10,10,10,10]
def demoitization(bannded,newcurrency,frequency):
    cashLimit=28000
    for i in range(len(arr)):
        if arr[i]==bannded:
            cashLimit-=arr[i]*freq[i]
            print(cashLimit)
            arr[i]=newcurrency
            freq[i]=frequency
            cashLimit+=newcurrency*frequency
            print(cashLimit)

demoitization(2000,1000,10)

