/*Write a program to find the smallest number divisible by all the 
numbers between 1 to 9*/

#include<bits/stdc++.h>
using namespace std;
int gcd(int num1, int num2)
{
    if (num2 == 0)
        return num1;
    return gcd(num2, num1 % num2);
}
int lcm(int arr[], int n)
{
    int res = arr[0];
    for (int i = 1; i < n; i++)
        res = (((arr[i] * res)) / (gcd(arr[i], res)));
    return res;
}
void smallestNumberDivBy1To9(){
    int arr[]={1,2,3,4,5,6,7,8,9};
    int res=lcm(arr,9);
    cout<<res;
}
int main(){
    smallestNumberDivBy1To9();
}