/*
Write a function that takes in a non-empty array of distinct integers and
 an integer representing a target sum. The function should find all triplets
  in the array that sum *up to the target sum* and return a two-dimensional
  array of all these triplets. The numbers in each triplet should be ordered
  in ascending order, and the triplets themselves should be ordered in
  ascending order with respect to the numbers they hold. If no three numbers
  sum up to the target sum, the function should return an empty array
*/
#include <bits/stdc++.h>
using namespace std;
void swap(int *num1, int *num2)
{
	int temp = *num1;
	*num1 = *num2;
	*num2 = temp;
}
void sort(int arr[], int n)
{
	int i, j;
	for (i = 0; i < n - 1; i++)
		for (j = 0; j < n - i - 1; j++)
			if (arr[j] > arr[j + 1])
				swap(&arr[j], &arr[j + 1]);
}

void AllTriplet(int arr[], int n, int sum)
{
	int **a = new int *[n]; // making 2d array with n rows
	for (int i = 0; i < n - 1; i++)
	{
		unordered_set<int> hash; // Hash Map
		for (int j = i + 1; j < n; j++)
		{
			int x = sum - (arr[i] + arr[j]);
			if (hash.find(x) != hash.end())
			{
				// cout << x << " " << arr[i] << " " << arr[j] << endl;
				a[i] = new int[3]; // make another array under the array named as 'a'
				a[i][0] = x;
				a[i][1] = arr[i];
				a[i][2] = arr[j];
				sort(a[i], 3);
			}
			else
				hash.insert(arr[j]);
		}
	}
	// Printing 2D Array
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			if(a[i][j]<1000000){
				cout << a[i][j] << " ";
			}
			else{
				break;
			}
		}
		cout << endl;
	}
}
int main()
{
	int arr[] = {12, 3, 4, 6, 1};
	int sum = 22;
	int n = sizeof(arr) / sizeof(arr[0]);
	AllTriplet(arr, n, sum);
	return 0;
}
