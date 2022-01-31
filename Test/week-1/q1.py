def strings(list):#string concatinate
    temp=''
    for i in range(len(list)):
        temp+=list[i]
    return temp
def printallagain(string1,string2,string,ptr1,ptr2,i):#printAllAgain
    if ptr2==0 and ptr1==0:
        print(strings(string))
    if ptr1!=0:
        string[i]=string1[0]
        printallagain(string1[1:],string2,string,ptr1-1,ptr2,i+1)
    if ptr2!=0:
        string[i]=string2[0]
        printallagain(string1,string2[1:],string,ptr1,ptr2-1,i+1)
    
def printall(string1,string2,ptr1,ptr2):
    string=[' ']*(ptr1+ptr2)
    printallagain(string1,string2,string,ptr1,ptr2,0)

# string1='ABCD'
# string2='EFGH'
string1=input()
string2=input()
leng1=len(string1)
leng2=len(string2)
printall(string1,string2,leng1,leng2)
