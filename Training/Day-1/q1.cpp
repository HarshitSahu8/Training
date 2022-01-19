/*Write down a method boolean isNameValid(String  name).
A name is valid if following conditions are satisfied:
• It does not contain any vowel more than once.
• If the name contains two ‘S’, then there is not any ‘T’ in between them (both in capital cases).
*/
#include <bits/stdc++.h>
using namespace std;

bool isNameValid(string s, int n)
{
    char vowel[]={'A','E','I','O','U'};
    int freq[] = {0, 0, 0, 0, 0};
    for (int i = 0; i < n; i++)
    {
        for(int j=0;j<5;j++){
            if(vowel[j]==s[i]){
                freq[j]+=1;
                if (freq[j]>=2){
                    return false;
                }
            }
        }
    }
    int flag=0;
    int *array = new int[n];//n size
    for(int i=0;i<n;i++){
        if(s[i]=='S'){
            for(int j=i;j<n;j++){
                if(s[j]=='T'){
                    flag=1;
                }
                else if(s[j]=='S' && flag==1){
                    return false;                   
                }    
            }
        }
    }
    return true;
}

int main()
{
    string s;
    cin >> s;
    int n = s.length();
    for(int i=0;i<n;i++){
        s[i]-=32;
    }
    // cout<<s;
    bool res = isNameValid(s, n);
    if(res){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
}