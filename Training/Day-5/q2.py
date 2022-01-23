'''
2. Write a program to print all the possible combinations according to the input values.
Example :
Given Values
'1' : ['Z', 'Y', 'A'],
'2' : ['B', 'O'],
'12' : ['L']
'3' : ['U', 'P']

Input : 123
Output : [ZBU, ZBP, ZOU, ZOP, YBU, YBP, YOU, YOP, ABU, ABP, AOU, AOP, LU, LP]

'''
# def combine(arr1,arr2):
#     combo=[]
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             combo.append(arr1[i]+arr2[j])
#     return combo

# def sub(inp):
#     l=['']*((len(inp)*2)-1)
#     c=0
#     for i in range(1,len(inp)):
#         for j in range(len(inp)-i+1):
#             end=j+i-1
#             temp=''
#             for k in range(j,end+1):
#                 temp+=inp[k]
#             l[c]=temp
#             c+=1

#     return l

def solve(values,inp,res,idx,n):
    if idx==n:
        print(res,end=' ')
        return
    dig=inp[idx]
    leng=len(values[dig])
    for i in range(leng):
        solve(values,inp,res+values[dig][i],idx+1,n) 


values = {'1': ['Z', 'Y', 'A'],
          '2': ['B', 'O'],
          '12': ['L'],
          '3': ['U', 'P']}
inp='123'
solve(values,inp,str(''),0,len(inp))

