def isNameValid(s):   
    vowel={'a':0,'e':0,'i':0,'o':0,'u':0,
    'A':0,'E':0,'I':0,'O':0,'U':0}
    s=s.upper()
    print(s)
    S=0
    for i in s:
        if i in vowel:
            vowel[i]=vowel[i]+1
            if vowel[i]==2:
                return False
    for i in s:
        if i=='S':
            S+=1
    if S>=2:
        st=0
        end=0
        #set st and end value:
        for i in range(len(s)):
            if s[i]=='S':
                st=i
                for j in range(i,len(s)):
                    if s[j]=='S':
                        end=j
                        if (end-st)>1:
                            for k in range(st,end):
                                if s[k]=='T':
                                    return False
    return True


print(isNameValid('fgdgfSbfffgfS'))

    