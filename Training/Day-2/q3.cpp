/*
Write a program to print the below pattern:
Q3 Write a program to print the below pattern:
(N should be an odd number and the value of N should be more than 4) 
N(Matrix Size N*N)
Output: 
//         \*****/
//         *\***/*
//         **\*/**
//         ***/***
//         **/*\**
//         */***\*
//         /*****\
//
/**/
#include <bits/stdc++.h>
using namespace std;
void drawPattern()
{
    int inp = 7;
    int start = 0;
    int end = inp-1;
    for (int i = 0; i < inp; i++)
    {
        for (int j = 0; j < inp; j++)
        {
            if(start==j && end==j){
                cout<<"/";
                start++;
                end--;
            }
            else if (i==j)
            {
                cout << "\\";
                start++;
            }
            else if(end==j)
            {
                cout<<"/";
                end--;
            }
            else {
                cout<<"*";
            }
        }
        cout<<endl;
    }
}
int main()
{
    drawPattern();
}