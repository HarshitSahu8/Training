'''
Make a StringUtils class which contains following methods
NOTE: You can use only String.charAt(), methods to code this problem.
(Don't use any other inbuilt functions)
static int countChar(String str,char ch)
- Returns occurrence of the given character in the given String (str).
static String substring(String str,int start,int end)
- Returns a substring from the start index to end index with all validation checks.
static String[] split(String str,char ch)
- Returns an array of strings broken according to the occurrence of the given character with 
validation checks.
static Boolean hasPattern(String str,String pattern)
- Returns true if the give string (pattern) found in the main string (str) otherwise false.
static Boolean allWordsContainsChar(String str,char ch)
- Returns true if all words of the given string (str) contains the given character (ch)  otherwise false.
static String reverse(String str)
- Returns the reverse of the String (Without using extra String or array)
static String reverseVowels(String str)
- Reverse only all the vowels in the string and return it ( Example : 
Input: s = "liipcoce"
Output: "leopcici"
Input: s = "hello"
Output: "holle"
)
'''
class StringUtils():
    def countChar(self, string, char):
        count = 0
        for i in range(len(string)):
            if string[i] == char:
                count += 1
        return count

    def substring(self, string, start, end):
        # print(string)
        leng = len(string)
        if (start > leng or end > leng) and (start < 0 and end < 0) and (start > end):
            print("invalid Input")
            return
        # I can do by 3 pointer approach(nxt time)
        for i in range(start, end+1):
            for j in range(end-i+1):
                k = j+end-1
                for k in range(i, end+1):
                    print(string[k], end='')
                print()
        return

    def splitByChar(self, string, ch):
        leng = len(string)
        temp = ''
        l = []
        for i in range(leng):
            if string[i] == ch:
                l.append(temp)
                temp = ''
            else:
                temp += string[i]
        for i in range(len(l)):
            print(l[i])
        return

    def hasPattern(self, string, pattern):
        leng = len(string)
        len_pat = len(pattern)
        if len_pat > leng:
            print("pattern grater than given string")
            return
        sptr = 0
        pptr = 0
        while(sptr < leng):
            if string[sptr] == pattern[pptr]:
                pptr += 1
            if pptr == len_pat-1:
                return True
            sptr += 1
        if pptr == len_pat-1:
            return True
        else:
            return False

    def AllWordsContainsChar(self, string, ch):
        leng = len(string)
        flag = 0
        for i in range(leng):
            if string[i] == ch:
                flag = 1
            if string[i] == ' ':
                if flag == 0:
                    return False
                else:
                    flag = 0
        if flag == 0:
            return False
        else:
            return True

    def reverse(self, string):
        leng = len(string)
        start = 0
        end = leng-1
        while(start < end):
            string = (string[:start] + chr(ord(string[start]) ^ ord(string[end])) +
                      string[start + 1:])
            string = (string[:end] + chr(ord(string[start]) ^
                                         ord(string[end])) +
                      string[end + 1:])
            string = (string[:start] + chr(ord(string[start]) ^
                                           ord(string[end])) +
                      string[start + 1:])
            start += 1
            end -= 1
        print(string)
    def reverseVowels(self,string):
        vowels={'a','e','i','o','u'}
        leng=len(string)
        l=['']*leng
        for i in range(leng):
            l[i]=string[i]
        start=0
        end=leng-1
        while(start<end):
            if l[start] in vowels and l[end] in vowels:
                l[start],l[end]=l[end],l[start]
                end-=1
                start+=1
            elif l[start] in vowels and l[end] not in vowels:
                end-=1
            elif l[end] in vowels and l[start] not in vowels:
                start+=1
            else:
                end-=1
                start+=1
        temp=''
        for i in range(len(l)):
            temp+=l[i]
        print(temp)
    
obj = StringUtils()
inp = 'leopcici'
tar = 'i'
# print(obj.countChar(inp,tar))
# obj.substring('abcdef',1,4)
# obj.splitByChar(inp,'i')
# print(obj.hasPattern(inp,'eop'))
# res=obj.AllWordsContainsChar('This Tac ackics','T')
# print(res)
# obj.reverse('string')
# obj.reverseVowels(inp)
