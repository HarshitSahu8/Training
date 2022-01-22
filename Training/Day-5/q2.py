'''
 Write a program to print all the possible combinations according to the input values.
Example :
Given Values
'1' : ['Z', 'Y', 'A'],
'2' : ['B', 'O'],
'12' : ['L']
'3' : ['U', 'P']

Input : 123
Output : [ZBU, ZBP, ZOU, ZOP, YBU, YBP, YOU, YOP, ABU, ABP, AOU, AOP, LU, LP]

'''
def combination(arr1,arr2):
    res=[[x,y] for x in arr1 for y in arr2]
    print(res)

Input = '123'
Hash = {'1': ['Z', 'Y', 'A'],
        '2': ['B', 'O'],
        '12': ['L'],
        '3': ['U', 'P']}
combination(Hash['1'],Hash['2'])



# a = ["foo", "bar"]
# >>> b = [1, 2, 3]
# >>> [(x,y) for x in a for y in b]  # for a list
# [('foo', 1), ('foo', 2), ('foo', 3), ('bar', 1), ('bar', 2), ('bar', 3)]
