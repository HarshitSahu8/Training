#include <iostream>
using namespace std;
int swapLastFirst(int num)
{
    int tempn=num%10;
    num=num%10;
    int rev =0;
    while(num>9){
        rev = rev *10 +(num%10);
        num=num/10;
    }
    while(rev >0){
        tempn=tempn*10+(rev%10);
        rev=rev/10;
    }
    tempn=tempn*10+num;
    return tempn;
}
int main()
{
    int res = swapLastFirst(123);
    cout<<res;
}