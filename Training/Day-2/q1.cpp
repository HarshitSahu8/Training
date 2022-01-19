/*Write a program to remove duplicate values from an array and returns 
an array of unique values. int[] removeDuplicates(int[]values)*/
#include <bits/stdc++.h>
using namespace std;

void removeDuplicates()
{
    int n;
    int maxNo = INT_MIN;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for (int i = 0; i < n; i++)
    {
        if(maxNo<arr[i]){
            maxNo=arr[i];
        }
        // maxNo = max(maxNo, arr[i]);
    }
    // cout<<"max: "<<maxNo<<endl;
    int *flag = new int(maxNo+1);
    for (int i = 0; i < maxNo+1; i++)
    {
        flag[arr[i]]=1;
    }
    for(int i=0;i<maxNo+1;i++)
    {
        if(flag[i]==1)
        {
            cout<<i<<" ";
        }
    }
}
int main()
{
    removeDuplicates();
}