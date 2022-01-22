#  '''
#  Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# s consists of English letters, digits, symbols and spaces.
# '''

def lg(s):
    start=0
    length=len(s)
    unique={}
    sets=[]
    temp=''
    while(start<length):
        if s[start] not in unique:
            temp+=s[start]
            unique[s[start]]=1
        elif s[start] in unique:
            sets.append(temp)
            # print(sets)
            temp=''
            unique.clear()
        start+=1
    l=[0]*len(sets)
    for i in range(len(sets)):
        l[i]=len(sets[i])
    maxi=0
    for i in range(len(l)):
        if maxi<l[i]:
            maxi=l[i]
    print(maxi)
    

lg('abcaarefabcd')