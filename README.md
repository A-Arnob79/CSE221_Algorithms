# CSE221_Algorithms

----------------------------------------------------------LAB - 01----------------------------------------------------------------------

A - Odd or Even
Do you know how to tell if a number is Odd or Even? You are given T numbers, and for each of those numbers, you have to tell whether the number is odd or even.
Input:
The first line will contain a single integer T(1≤T≤100). Each of the next T lines will contain a number N(-10^5 ≤N≤ 10^5).
Output:
For each N, you have to print whether the number is odd or even. Please see the sample input-output format to know what exactly you have to print.

Examples:
Input:                             Output:
5                                  5 is an Odd number.
10                                 10 is an Even number.
19                                 19 is an Odd number.
7                                  7  is an Odd number.
3                                  3 is an Odd number.
100                                100 is an Even number.





B - Can you solve Arithmetic Expressions? 
Can you solve arithmetic expressions with your programming knowledge? Let's find it out. You will be given some arithmetic expressions, and you have to solve them.
Input:
The first line will contain a number T(1≤T≤1000) representing the number of test cases. Then for each test case, you will be given an arithmetic expression. Please see the sample input below. It is guaranteed that the numbers inside the arithmetic expression will be between 1 and 1000.
Output
For each test case, you have to print the result. Look at the sample output for reference.

Important Note: Your answer might contain floating point numbers, and in that case, your answer doesn't have to be exactly equal to the actual answer. For example, if your answer is 20.250000001 and the judge's solution is 20.25, your answer will still be considered correct. As long as it is really close to the correct solution, your solution will be considered correct. Formally speaking, if your solution is x, and the judge's solution is y, then as long as ∣x−y∣≤10^−6, your solution will be correct. In the above example, your solution was 20.250000001 and the judge's solution was 20.25. If you take the difference of these two numbers,  they are smaller than 10^−6. Similarly, if the judge's solution is 19.0000000000 and your solution is 19, it is still correct, as the difference is 0, which is less than 10^−6.
Examples:
Input:
15
calculate 67 + 41
calculate 85 / 5
calculate 13 - 56
calculate 99 - 95
calculate 3 / 10
calculate 12 * 19
calculate 14 - 6
calculate 3 * 88
calculate 45 * 68
calculate 81 - 0
calculate 77 + 40
calculate 8 * 84
calculate 73 - 22
calculate 85 - 86
calculate 28 * 58
Output:
108.000000
17.000000
-43.000000
4.000000
0.300000
228.000000
8.000000
264.000000
3060.000000
81.000000
117.000000
672.000000
51.000000
-1.000000
1624.000000





C - Array Reverse 
You are given an array of N integers. Your task is to reverse the array and print the last K integers from the reversed array.
Input:
The first line contains two integers N(1≤N≤10^6) and K(1≤K≤N) — the number of elements in the array and the value K.
The second line contains N integers separated by spaces a1,a2,a3…an (1 ≤ai ≤10^6) — the elements of the array.
Output:
Print K space separated integers as described in the statement.
Examples:
Input1:
5 3
5 6 7 8 9
Output1:
7 6 5 
Input2:
8 5
20 8 9 3 10 7 100 12
Output2:
10 3 9 8 20 





D - Fast Sum
Your friend is trying to solve the following problem. You are given T test cases. For each test case, you are given an integer N. You have to find out the summation of 1 to N. Your friend wrote the following Python code to solve it:

T = int(input())

for _ in range(T):
    N = int(input())
    sum = 0
    for i in range(1, N + 1):
        sum += i
    print(sum)

However, the code is not passing the online judge due to some unknown errors for large values of N.
Since you are currently studying CSE221 and have learned about time complexity, help your friend come up with a more efficient solution.

Input:
The first line contains a single integer T(1≤T≤10^4) — the number of test cases. The next T lines each contain a single integer N(1≤N≤10^6).
Output:
For each test case, print a single integer — the summation from 1 to N.
Examples:
Input:                           Output:
5                                3
2                                15
5                                55
10                               78
12                               5050                          
100





E - Bubble Sort? 
Here is the code of bubble sort. Its run time complexity is θ(n^2). Change the code in a way so that its time complexity is θ(n) for the best-case scenario. You are not allowed to use any builtin sort function to solve this problem.

def bubbleSort(arr):                                                    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

Input:
In the first line, you will be given 
N(1≤N≤10^5). Then you will be given an array 
a of N integers (1≤ai≤10^9) that you have to sort in increasing order. It is guaranteed that if the original input array is not in the best case scenario, 1≤N≤1000.
Output:
Output the sorted array (Please see the sample output for reference)
Examples:
Input1:
5
3 2 1 4 5
Output1:
1 2 3 4 5 
Input2:
6
5 10 15 20 25 30
Output2:
5 10 15 20 25 30 





F - Sorting Again?? 
Suppose you are given a task to rank the students. You have gotten the marks and ID of the students. Now your task is to rank the students based on their marks using a sorting algorithm. If two or more students get the same mark, then students with the lower ID will get prioritized. See the input and output for a better understanding.
However, you have to keep in mind that your sorting algorithms perform the minimum number of swapping operations.

Input:
The first line of the input file will contain an integer N(1≤N≤1000). The second line will contain N integers, representing the Student ID, Si(1≤ Si ≤1000). The next line will contain the N integers, Sm(1≤Sm≤1000), which denotes the obtained mark of the corresponding students.
Note: It is guaranteed that the student IDs are unique. 

Output:
The first line of the output must contain a number X which denotes the number of minimum swaps. The rest of the N lines will contain the Student ID and obtained marks sorted based on the instruction above. See the sample output for a better understanding.
Important Note: Since you are asked to minimize the number of swaps, if your number of swaps doesn't match with the judge's answer, your solution will be considered incorrect.
Look at the first sample input. It can be shown that this can be sorted with only 4 swaps. It can also be shown that it is not possible to sort this in less than 4 swaps.

Examples:
Input1:
7
7 4 9 3 2 5 1
40 50 50 20 10 10 10
Output1:
Minimum swaps: 4
ID: 4 Mark: 50
ID: 9 Mark: 50
ID: 7 Mark: 40
ID: 3 Mark: 20
ID: 1 Mark: 10
ID: 2 Mark: 10
ID: 5 Mark: 10
Input2:
4
7 2 5 3
80 60 80 50
Output2:
Minimum swaps: 2
ID: 5 Mark: 80
ID: 7 Mark: 80
ID: 2 Mark: 60
ID: 3 Mark: 50





G - Trains? 
You have been recently recruited as the Software Engineer at Jumanji Railway Software System. You have a big task at hand. You will be given N(1≤N≤100) schedule of the train. The next N line will contain the name of the train and the departure time. See the input format for better understanding.

Your task is to write a sorting algorithm that will group the trains in the lexicographical order based on the name of the trains. If two or more trains have the same name, then the train with the latest departure time will get prioritized. If there is still a tie, then the train which comes first in the input will come first.

Input:
The first line will contain an integer N(1≤N≤100). For the next N lines, ith line will describe ith train. Please see the sample input for better understanding.
Please note that the names of the trains and destinations don't contain any white spaces, and the length of the names and destinations will be at most 100. For example, look at the following description: DhumketuExpress will departure for Chittagong at 02:30
Here, DhumketiExpress is the name of the train Chittagong is the destination, and they don't contain any whitespaces, and their length is less than 100.

Output:
Print the train description in the sorted order (specified above). Please see the output format for better understanding.

Examples:
Input:
8
ABCD will departure for Mymensingh at 00:30
DhumketuExpress will departure for Chittagong at 02:30
ABC will departure for Dhaka at 17:30
ABCD will departure for Chittagong at 01:00
ABC will departure for Khulna at 03:00
ABC will departure for Barisal at 03:00
ABCE will departure for Sylhet at 23:05
PadmaExpress will departure for Dhaka at 19:30

Output:
ABC will departure for Dhaka at 17:30
ABC will departure for Khulna at 03:00
ABC will departure for Barisal at 03:00
ABCD will departure for Chittagong at 01:00
ABCD will departure for Mymensingh at 00:30
ABCE will departure for Sylhet at 23:05
DhumketuExpress will departure for Chittagong at 02:30
PadmaExpress will departure for Dhaka at 19:30

----------------------------------------------------------LAB - 02----------------------------------------------------------------------

A - Two Sum Trouble
[Time limit per test1 second
memory limit per test256 megabytes]

Your little brother, Bob, loves playing with integers. One day, his teacher gave him a sorted list of N integers in non-decreasing order. Now, your brother wants to play a game with you.

Bob will give you an integer S. You have to find if it is possible to find two values from the list (at distinct positions) whose sum is equal to S. Since you are feeling very tired, you decide to write a program that can quickly answer Bob's query.

Input:
The first line contains two integers N (1≤N≤106)
 and S (1≤S≤109), denoting the length of the list, and the target Sum.

In the next line, there will be N integers a1,a2,a3…an
 (1≤ai≤109)
 in non-decreasing order, separated by spaces.

Output:
Print two distinct 1-based indices i and j such that ai+aj=S
 where i<j. If no such pair exists, then print -1. If multiple solutions exist, you may print any one of the valid answers.

Examples:
Input
4 10
1 3 5 7
Output
2 4

Input
6 18
1 5 8 9 9 10
Output
3 6

Input
4 7
2 4 6 8
Output
-1

Input
4 10
1 5 6 8
Output
-1





B - A Beautiful Sorted List
[Time limit per test1 second
memory limit per test1024 megabytes]

Alice and Bob are two friends. Alice has a list of length N in non-decreasing order, and Bob has a list of length M, also in non-decreasing order.Now, they want to combine their lists into a single non-decreasing list of length N+M. However, they are not very good at algorithms, so they asked for your help.

Since you are a computer science student, your task is to write an efficient algorithm to merge the two given lists into one non-decreasing list. Solve the problem in O(N+M).

Input:
The first line contains an integer N (1≤N≤106), denoting the length of Alice's list.
The second line contains N space-separated integers representing Alice's list.
The third line contains an integer M (1≤M≤106), denoting the length of Bob's list.
The fourth line contains M space-separated integers representing Bob's list.
All the numbers given in the input will fit within a 32-bit signed integer. It is guaranteed that the given lists will be in non-decreasing order.

Output:
You have to make a sorted list in non-decreasing order from the given lists and show the output.

Examples:
Input:
4
1 3 5 7
4
2 2 4 8
Output:
1 2 2 3 4 5 7 8 

Input:
3
2 10 12
6
3 4 6 7 8 9
Output:
2 3 4 6 7 8 9 10 12 

Input:
5
1 2 3 4 5
2
10 12
Output:
1 2 3 4 5 10 12 

Input:
4
1 2 12 13
3
10 15 18
Output:
1 2 10 12 13 15 18 

Input:
8
1 2 3 8 8 10 12 14
9
1 1 4 5 6 8 13 15 16
Output:
1 1 1 2 3 4 5 6 8 8 8 10 12 13 14 15 16 





C - Longest Subarray Sum
[Time limit per test1 second
memory limit per test256 megabytes]
You are given an array of N integers and an integer K. Your task is to find the length of the longest contiguous subarray whose sum is less than or equal to K.

Input:
The first line contains two integers N (1≤N≤105)
 and K (1≤K≤109)— the size of the array and the maximum allowed sum.
The second line contains N space-separated integers a1,a2,a3…an(1≤ai≤106)— the elements of the array.

Output:
Print a single integer — the length of the longest contiguous subarray whose sum is less than or equal to K.

Examples:
Input:
5 4
4 1 2 1 5
Output:
3

Input:
5 5
1 1 1 1 1
Output:
5

Input:
3 1
2 3 4
Output:
0

Input:
10 12
1 2 6 4 3 2 3 1 4 2
Output:
5

Note:
In the first example, possible subarrays with sum less than or equal to 4 are [4],[1],[2],[1],[1,2],[2,1],[1,2,1]. Among them, the longest size is 3.
In the second example, sum of the entire array is 5. Hence, we can take the whole array.
In the third example, no subarray has sum less than or equal to 1. Hence, the answer is 0.





D - Can you Iterate the Binary String?
[Time limit per test0.5 seconds
memory limit per test256 megabytes]
You are given T test cases. Each test case contains a binary string S that follows a specific pattern:
There will be zero or more 0s in the prefix of S.
There will be zero or more 1s in the suffix of S.
For each string, find the index of the first occurrence of the character 1 in the 1-based indexing. Find the output of each query in O(log|S|).

Input:
The first line contains an integer T (1≤T≤104)— the number of test cases. Each of the next T lines contains a binary string S (1≤|S|≤4×103), where |S| represents the length of the string.

Output:
For each test case, print a single integer:
The first occurrence of the character 1 in the string S in the 1-based indexing.
If there is no 1 in the string, print −1.

Examples:
Input:
15
0000011111111
00000111111111
00000
0000
1111
111
0
1
01
01111
000000000000001
0000000000000001
0000000000000111111111111111111111
00000001111111111111111
0000000111111111111111111111111111
Output:
6
6
-1
-1
1
1
-1
1
2
2
15
16
14
8
8





E - Count the Numbers
[Time limit per test1 second
memory limit per test256 megabytes]
You are given a sorted array a of n elements, and some queries. In each query, you are given a pair [x,y] and you have to count how many numbers ai are there such that x≤ai≤y. For example, if the array is [10,20,20,45,79] and you are given a query [20,50], then answer will be 3 because there are in total 3 numbers that's value is between 20 and 50.

Input:
The first line of the input contains n(1≤n≤105) and q(1≤q≤105) denoting the array size and the number of queries respectively. The next line will contain the array elements separated by space where 1≤ai≤109 where i=0,1,2,…,n−1. Each of the next q lines will contain a pair [x,y] where 1≤x≤y≤109. See the sample input format for better understanding.

Note1: It is guaranteed that the given array is sorted in non-decreasing order.
Note2: It is also guaranteed that the queries are valid. Which means, for each query [x,y], x≤y.

Output:
For each query [x,y], output a single integer P denoting the number of elements in the array a such that x≤ai≤y.

Example:
Input:
5 3
10 20 20 45 79
20 50
5 45
1 100
Output:
3
4
5

----------------------------------------------------------LAB - 03----------------------------------------------------------------------

A - Count the Inversion
[Time limit per test1 second
memory limit per test256 megabytes]

Here is a Pseudocode of the Merge Sort Algorithm.
def merge(a, b):
    # write your code here
    # a and b are two sorted list
    # merge function will return a sorted list after merging a and b

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(............)  # write the parameter 
        a2 = mergeSort(............)  # write the parameter
        return merge(a1, a2)          # complete the merge function above 

Now, you are given an array A of size N of N distinct integers. It is guaranteed that the array A contains a permutation of integers from 1 to N (i.e., every integer from 1 to N appears exactly once).

Count the number of inversions in the given array.
Sort the array in non-decreasing order.
An inversion is a pair (i,j) where i<j and A[i]>A[j].

Input:
The first line contains an integer N (1≤N≤105) — denoting the length of the list.
In the next line, there will be N integers a1,a2,a3…an (1≤ai≤N) separated by spaces.

Output:
In the first line, print the total number of inversions in the given array. In the next line, print the array in non-decreasing order.

Example:
Input:
5
1 2 5 4 3
Output:
3
1 2 3 4 5 
Input:
5
1 2 3 4 5
Output:
0
1 2 3 4 5 
Input:
5
5 4 3 2 1
Output:
10
1 2 3 4 5 
Input:
7
6 4 2 5 7 3 1
Output:
14
1 2 3 4 5 6 7 

Note:
In the first example, the inversions are pair (3,4),(3,5) and (1,5). In the second example, there are no inversions. In the third example, every pair of i,j where i<j, we have A[i]>A[j]. Hence, All 10 such pairs are inversions.





B - Pair Maximization
[Time limit per test1 second
memory limit per test256 megabytes]

you are given an array A of size N. You have to choose two indices i and j such that 1≤i<j≤N and A[i]+A[j]2 is the maximum possible. Here, we are considering 1-based indexing. Come up with a divide and conquer approach to solve the problem.

Input:
The first line contains an integer N (2≤N≤105)— denoting the length of the list.
In the next line, there will be N integers A1,A2,A3…An (−109≤Ai≤109) separated by spaces.

Output:
Print a single integer - which denotes the maximum possible value of A[i]+A[j]2.

Examples:
Input:
5
4 3 1 5 6
Output:
41

Input:
5
4 3 1 -9 6
Output:
85





C - Fast MOD Drift
[Time limit per test1 second
memory limit per test256 megabytes]

You are given two integers a and b. Calculate abmod107.
Input:
The input file contains two integers a (1≤a≤104) and b (1≤b≤1012).

Output:
Print one integer — the result of abmod107.

Examples:
Input:
100 3
Output:
85
Input:
100 5
Output:
99
Input:
10000 1000000000000
Output:
27





D - Fast MOD Drift Revisited
[time limit per test2.5 seconds
memory limit per test256 megabytes]

You are given three integers a, n and m. Calculate (a1+a2+…+an)%m.
Input:
The first line contains an integer T (1≤T≤105)— total numbers of test cases.
In each of the next T test cases, there are three integers a (1≤a≤106), n (1≤n≤1012) and (1≤m≤109)
Output:
Print one integer — the result of (a1+a2+…+an)%m.

Example:
Input:
3
2 5 1000
2 9 1000
1 100 30

Output:
62
22
10





E - Ordering Binary Tree
[Time limit per test1 second
memory limit per test256 megabytes]

you are given an array A of size N in increasing order. Find an order of these N integers such that, if these integers are inserted into a Binary Search Tree (BST) one by one, the height of the resulting BST is minimized.
A Binary Search Tree is a binary tree in which each node has at most two children, referred to as the left and right child. For any node, all elements in the left subtree are smaller than the node's value, and all elements in the right subtree are greater than the node's value.
The height of a Binary Search Tree is defined as the maximum depth among all the nodes in the tree.
Note: All the elements in the array A are guaranteed to be unique. In other words, Ai≠Aj if i≠j.

Input:
The first line contains an integer N (1≤N≤105) — denoting the length of the list.
In the next line, there will be N integers a1,a2,a3…an (1≤ai≤109) in non-descending order separated by spaces.

Output:
Output the order of the elements such that when inserted into a Binary Search Tree, the height of the tree is minimized. If there are multiple such orders then find any of them.

Example:
Input:
5
1 2 3 4 5
Output:
3 1 2 4 5 





F - 220 Trees
[Time limit per test1 second
memory limit per test256 megabytes]
There is a Binary Tree with N nodes. You are given the in–order and pre-order traversals of the tree. Your task is to determine the post-order traversal of the tree.

Input:
The first line contains an integer N (1≤N≤1000) — the number of nodes in the binary tree.
In the next line, there will be N integers a1,a2,a3…an (1≤ai≤N) separated by spaces – representing the in-order traversal of the tree.

The following line, there will be N integers b1,b2,b3…bn (1≤bi≤N) separated by spaces – representing the pre-order traversal of the tree.

Output:
Print N space-separated integers representing the post-order traversal of the binary tree.

Example:
Input:
5
4 2 5 1 3
1 2 4 5 3
Output:
4 5 2 3 1 

----------------------------------------------------------LAB - 04----------------------------------------------------------------------







