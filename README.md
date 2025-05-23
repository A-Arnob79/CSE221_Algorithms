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

A - Adjacency Matrix Representation
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a direct connection between two nodes. There is no self loop or multi edge.

Input:
The first line contains two integers N and M (1≤N≤100,0≤M≤N(N−1)2) — the number of vertices and the total number of edges.
The next M lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤1000) — denoting there is an edge from node ui to vi with cost wi.

Output:
The output consists of an N×N adjacency matrix representing the directed weighted graph. Each row corresponds to a node, and each column represents its directed edges to other nodes. The value at position (i,j) denotes the weight of the edge from node i to node j. If there is no edge, the value is 0.

Examples:
Input:
6 7
1 5 6
6 3 5
1 3 9
3 4 7
4 6 1
5 6 8
6 1 6
Output:
0 0 9 0 6 0 
0 0 0 0 0 0 
0 0 0 7 0 0 
0 0 0 0 0 1 
0 0 0 0 0 8 
6 0 5 0 0 0 

Input:
4 3
1 3 8
3 2 5
1 4 2
Output:
0 0 8 2 
0 0 0 0 
0 5 0 0 
0 0 0 0 





B - Adjacency List Representation
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Each edge represents a direct connection between two nodes. There is no self loop or multi edge.

Input:
The first line contains two integers N and M (1≤N≤100,0≤M≤N(N−1)2) — the number of vertices and the total number of edges.
The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.
The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the i-th edge.
Thr fourth line contains M integers w1,w2,w3…wm (1≤wi≤1000) — where the i-th integer represents the weight of the i-th edge.
The i'th edge of this graph is from the i'th node in the second line to the i'th node in the third line, their weight is the i'th value in the fourth line.

Output:
For the given input, the output should be the Adjacency List representation of the graph as shown in the sample output.

Examples:
Input:
4 5
4 1 4 3 3
3 2 2 2 1
4 4 10 8 5
Output:
1: (2,4)
2:
3: (2,8) (1,5)
4: (3,4) (2,10)
Input:
4 4
3 3 2 4
2 1 1 3
9 5 8 10
Output:
1:
2: (1,8)
3: (2,9) (1,5)
4: (3,10)





C - Graph Metamorphosis
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed unweighted graph with N nodes in an adjacency list format. The nodes are numbered from 0 to N-1. Your task is to convert it into an adjacency matrix representation.

Input:
The first line contains a integer N (1≤N≤100) — the number of vertices.
The next N lines describe the adjacency list:
The i-th line starts with an integer k, indicating the number of nodes adjacent to node i.
The next k space-separated integers represent the nodes adjacent to node i.
Nodes are numbered from 0 to N-1.

Output:
Print an N×N adjacency matrix, where the cell at row i and column j
1 if there is an edge between nodes i and j
0 otherwise.

Examples:
Input:
5
2 1 2
1 0
1 0
1 4
1 3
Output:
0 1 1 0 0 
1 0 0 0 0 
1 0 0 0 0 
0 0 0 0 1 
0 0 0 1 0 
Input:
5
0
2 2 3
3 1 3 4
2 1 2
1 2
Output:
0 0 0 0 0 
0 0 1 1 0 
0 1 0 1 1 
0 1 1 0 0 
0 0 1 0 0 





D - The Seven Bridges of Königsberg
[Time limit per test1 second
memory limit per test256 megabytes]

You are given an undirected unweighted connected graph with N nodes and M edges. There can be self loop or multiple edges. Your task is to determine whether an Eulerian Path exists in the graph.
In graph theory, an Eulerian path (also called an Eulerian trail or Eulerian walk) is a path in a graph that visits every edge exactly once and may start and end at different vertices. However, a vertex can be visited multiple times.

Input:
The first line contains two integers N and M (1≤N≤2×105,0≤M≤3×105) — the number of vertices and the total number of edges.
The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.
The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the i-th edge.
The i'th edge of this graph is between the i'th node in the second line and the i'th node in the third line.

Output:
If an Eulerian Path exists, print YES. Otherwise, print NO.

Examples:
Input:
5 10
5 5 5 2 2 2 3 3 4 2
2 3 1 3 4 1 4 1 2 4
Output:
YES
Input:
5 4
1 4 3 2
4 3 2 5
Output:
YES
Input:
8 7
4 4 6 6 3 1 8
6 5 3 2 7 8 7
Output:
NO
Input:
7 6
3 5 7 6 4 2
5 7 6 4 2 1
Output:
YES





E - Edge Queries
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. Your task is to find the difference of indegree and outdegree of each node in the graph.

Input:
The first line contains two integers N and M (1≤N≤2×105,0≤M≤3×105) — the number of vertices and the total number of edges.
The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.
The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the i-thedge.
The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

Output:
Output a single line with N space-separated integers, where the i-th integer is the difference of indegree and outdegree of node i.

Examples:
Input:
5 10
2 5 4 3 2 4 3 4 1 3
5 1 5 5 1 2 2 1 3 4
Output:
2 0 -2 -2 2
Input:
5 4
5 3 3 2
1 1 2 4
Output:
2 0 -2 1 -1
Input:
8 7
7 7 7 2 1 4 1
2 6 3 4 2 8 5
Output:
-2 1 1 0 1 1 -3 1





F - The King of Königsberg
[Time limit per test1 second
memory limit per test256 megabytes]

You are given an N∗N chessboard and the initial position (x,y) of a King piece. The King can move one step in any of the 8 possible directions: Up, Down, Left, Right, Top-left diagonal, Top-right diagonal, Bottom-left diagonal, Bottom-right diagonal.
Your task is to determine the number of valid moves the King can make in one move. A move is valid if it remains inside the board.

Input:
The first line contains an integer (1≤N≤2×105) — the size of the chessboard.
The second line contains two integers (1≤x,y≤N) — the initial position of the King on the chessboard.

Output:
First, print an integer K — the number valid moves the King can make in one move.
Next, print K lines, each containing two integers representing a valid move in ascending order. A move (a,b) is smaller than (c,d) if a<c or if a=c and b<.

Examples:
Input:
8
1 1
Output:
3
1 2
2 1
2 2
Input:
8
1 2
Output:
5
1 1
1 3
2 1
2 2
2 3
Input:
8
2 2
Output:
8
1 1
1 2
1 3
2 1
2 3
3 1
3 2
3 3





G. Coprime Graph
[Time limit per test2 seconds
memory limit per test256 megabytes]

You are given an integer N. Construct an undirected graph with N nodes, where each node i is connected to all node j such that gcd(i,j)=1 where 1≤i,j≤N and i≠j.

For example,for N=6, the graph will be, G= [[2,3,4,5,6], [1,3,5], [1,2,4,5], [1,3,5], [1,2,3,4,6], [1,5]].

Now, there will be Q queries. Each query consists of two integers X and K. For each query, you have to determine the K−th smallestnode connected to node X.

Input:
The first line contains two integers N and Q (1≤N≤2×103,1≤Q≤3×105) — the number of vertices and the total number of queries.
The next Q lines contain two integers X and K (1≤X≤N,1≤K≤106), representing a query.

Output:
For each query, output the K−th smallest node connected to node X. If there are fewer than K neighbors of X, then print -1.

Examples:
Input:
5 6
1 3
3 1
4 2
5 5
3 4
5 2
Output:
4
1
3
-1
5
2
Input:
2000 3
903 24
702 563
942 50
Output:
41
1829
149
Input:
1 1
1 1
Output:
-1
Input:
2 1
2 1
Output:
1

Note:
Explanation of the First Sample (Let's go through the queries):
Query (1, 3): The neighbors of node 1 are [2, 3, 4, 5]. Sorted: [2, 3, 4, 5]. The 3rd smallest is 4. Output: 4.
Query (3, 1): The neighbors of node 3 are [1, 2, 4, 5]. Sorted: [1, 2, 4, 5]. The 1st smallest is 1. Output: 1.
Query (4, 2): The neighbors of node 4 are [1, 3, 5]. Sorted: [1, 3, 5]. The 2nd smallest is 3. Output: 3.
Query (5, 5): The neighbors of node 5 are [1, 2, 3, 4]. There are only 4 neighbors, so the 5th smallest does not exist. Output: -1.
Query (3, 4): The neighbors of node 3 are [1, 2, 4, 5]. Sorted: [1, 2, 4, 5]. The 4th smallest is 5. Output: 5.
Query (5, 2): The neighbors of node 5 are [1, 2, 3, 4]. Sorted: [1, 2, 3, 4]. The 2nd smallest is 2. Output: 2.

----------------------------------------------------------LAB - 05----------------------------------------------------------------------

A - Can you Traverse-1?
[Time limit per test5 seconds
memory limit per test256 megabytes]

You are given an undirected unweighted graph with N cities and M roads. The cities are numbered from 1 to N. You may assume, the graph is connected, meaning there is a path between any pair of cities. There are no self-loops (no road connects a city to itself) and no multiple edges between the same pair of cities.
Your task is to perform a Breadth-First Search (BFS) starting from node 1 and print the order in which the nodes are visited.

Input:
The first line contains two integers N and M (1≤N≤2×10^5,1≤M≤3×10^5) — the number of cities and the total number of roads.

The next M lines will contain two integers ui,vi(1≤ui,vi≤N) — denoting there is an edge between city ui and city vi.

Output:
Print the BFS traversal starting from node 1 as a space-separated list of visited nodes. If there are multiple BFS path traversal order, you may print any.

Examples:
Input:
4 3
1 4
3 2
1 3
Output:
1 3 4 2
Input:
6 10
3 1
1 6
6 4
4 5
5 2
6 2
4 3
5 6
3 6
1 5
Output:
1 3 5 6 4 2
Input:
4 5
1 3
3 4
4 2
3 2
1 4
Output:
1 3 4 2





B - Can you Traverse-2?
[Time limit per test1 second
memory limit per test1024 megabytes]

You are given an undirected unweighted graph with N cities and M roads. The cities are numbered from 1 to N. The graph is connected, and contains no self-loops or multiple edges.

Your task is to perform a Depth-First Search (DFS) starting from node 1 and print the order in which the nodes are visited.

Input:
The first line contains two integers N and M (1≤N≤2×105,1≤M≤3×105) — the number of cities and the total number of roads.

The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.

The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the 
i-th edge.

The i-th edge of this graph is between the i-th node in the second line and the i-th node in the third line.

Output:
Print the DFS traversal starting from node 1 as a space-separated list of visited nodes. If there are multiple DFS path traversal order, you may print any.

Examples:
Input:
4 3
1 3 1
4 2 3
Output:
1 3 2 4 
Input:
6 8
1 5 3 4 6 1 6 4
5 3 4 6 2 3 3 1
Output:
1 3 4 6 2 5 
Input:
5 7
5 1 3 2 4 4 4
1 3 2 4 1 3 5
Output:
1 3 2 4 5 





C - Lightning McQueen
[Time limit per test1 second
memory limit per test256 megabytes]
You are given an undirected unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self loops or multiple edges.

There is a source and a destination. Your task is to find the shortest distance from the source node to destination node and print the path taken. If multiple shortest paths exist, print the one that is lexicographically smallest.

A path P1=[a1,a2,…an] is lexicographically smaller than a path P2=[b1,b2,…bm] if at the first position where they differ, ai<bi. For example, [1,4,3] is smaller than [1,5,7,1].
If no path exists, print −1.

Input:
The first line contains four integers N,M,S,D (1≤N≤2×10^5,0≤M≤3×10^5,1≤S, D≤N) — the number of vertices, total number of edges, source and destination.

The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.

The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is other endpoint of the i-th edge.

The i-th edge of this graph is between the i-th node in the second line and the i-th node in the third line.

Output:
If a path exists, print the length of the shortest path (number of edges) on the first line.
On the second line, print the lexicographically smallest shortest path from source to destination.
If no path exists, print -1.

Examples:
Input:
5 10 5 3
2 1 5 3 1 4 2 4 1 4
5 5 4 5 2 2 3 1 3 3
Output:
1
5 3
Input:
5 4 2 5
5 1 2 4
1 3 3 2
Output:
3
2 3 1 5
Input:
8 7 3 2
7 7 3 2 2 8 5
2 6 7 4 1 4 1
Output:
2
3 7 2
Input:
6 6 6 5
1 2 1 5 5 3
5 1 4 2 4 2
Output:
-1
Input:
1 0 1 1


Output:
0
1





D - Through the Jungle
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self loops or multiple edges.

You have to find a shortest path from node S to node D that passes through node K. If multiple such paths exist, print any one of them. If no such path exists, print −1.

Input:
The first line contains five integers N,M,S,D,K (1≤N≤2×10^5,1≤M≤3×10^5,1≤S, D,K≤N) — the number of vertices, total number of edges, source, destination and the mandatory node that must be included in the path.

The next M lines will contain two integers ui,vi(1≤ui,vi≤N) — denoting there is an edge from city ui to city vi.

Output:
If a valid path exists from S to D through K, print the length of the path (number of edges) on the first line.
On the second line, print the nodes in the path in order from S to D.
If no such path exists, print −1.

Examples:
Input:
5 10 5 3 5
2 5
5 1
4 5
3 5
1 2
2 4
3 2
1 4
1 3
3 4
Output:
2
5 1 3
Input:
5 4 2 5 3
5 1
3 1
2 3
2 4
Output:
-1
Input:
8 7 3 2 4
7 2
6 7
7 3
2 4
1 2
8 4
5 1
Output:
-1
Input:
6 6 2 2 2
5 1
1 2
1 4
5 2
4 5
3 2
Output:
0
2





E - Cycle Detection
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a directed unweighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.

Write a code to find if there is any cycle in the graph. In graph theory, a cycle in a graph is a non-empty trail in which only the first and last vertices are equal.

Input:
The first line contains four integers N and M (1≤N≤2×10^5,1≤M≤2×10^5) — the number of vertices and total number of edges.
The next M lines will contain two integers ui,vi(1≤ui,vi≤N) — denoting there is an edge from city ui to city vi.

Output:
Print YES if the graph contains any cycle, otherwise print NO.

Examples:
Input:
4 7
1 3
1 2
2 4
3 1
2 3
4 3
4 1
Output:
YES
Input:
6 5
6 4
6 3
4 5
6 2
4 1
Output:
NO





F - Diamonds under W
[Time limit per test1 second
memory limit per test256 megabytes]

You are given a 2D grid with R rows and H columns.

Each cell in the grid is one of the following:
.— Empty cell: You can move into this cell.
D— Cell with a diamond: You can move into this cell and collect the diamond.
#— Obstacle: You cannot move into this cell.

You may start from any non-obstacle cell and move in the four directions: up, down, left, or right. Your goal is to choose a starting cell such that you can collect the maximum number of diamonds

Input:
The first line contains two integers R and H (1≤R,H≤1000)— the number of rows and columns of the grid. The next Rlines each contain H characters, describing the grid.

Output:
Print a single integer — the maximum number of diamonds you can collect starting from a valid cell.

Examples:
Input:
5 5
.#.DD
##.#.
####D
#DDD#
#..DD
Output:
5
Input:
5 5
D####
##.D#
#..D#
###D#
..##D
Output:
3
Input:
5 5
.....
####.
#..#.
####.
.....
Output:
0
Input:
1 5
D....
Output:
1
Input:
9 11
.#..D...D..
.#.#######.
D#.#..D..#.
D#D#.###.#D
.#.#..D#.#.
.#.#####.#D
D#..D...D#.
.#########.
...D..D...D
Output:
15

----------------------------------------------------------LAB - 06----------------------------------------------------------------------

A - Advising
[Time limit per test1 second
memory limit per test1024 megabytes]

In this problem, there are N courses in the curriculum and M requirements of the form "Course A has to be completed before course B".
Your task is to find an order in which you can complete the courses. If there are multiple valid order, you may print any of them. If no such sequence exists, then print −1.

Input:
The first line contains two integers N,M (1≤N≤2×10^5,1≤M≤3×10^5) — the number of courses and total requirements.
The next M lines will contain two integers Ai,Bi(1≤Ai,Bi≤N) — Course A has to be completed before course B.

Output:
Print an order in which you can complete the courses. Please note, that there could be multiple correct sequences. You can print any valid order that includes all the courses.
If there is no valid sequence, print −1.

Examples:
Input:
5 4
2 4
2 5
4 3
1 5
Output:
2 4 3 1 5
Input:
8 8
6 4
6 2
4 2
2 1
1 7
7 5
5 8
8 3
Output:
6 4 2 1 7 5 8 3
Input:
2 1
1 2
Output:
1 2
Input:
4 6
1 2
1 3
4 1
2 3
2 4
4 3
Output:
-1





B - A Football Match
[ime limit per test2 seconds
memory limit per test1024 megabytes]

There is an intense football match going on between Robots and Humans. However, things aren't as simple as they seem — the Robots have disguised themselves to look exactly like Humans! From the outside, it's impossible to tell who is a Robot and who is a Human.
The audience know only one important information — the Robots tackles only the Humans, and the Humans tackles only the Robots.
Now, you are given a list of tackles, each involving two players. Based on this information, find the maximum possible number of Robots or Humans.

Input:
The first line contains two integers N and M (1≤N≤2×10^5,1≤M≤3×10^5) — the number of players in the match and the number of tackles occurred during the match respectively.
The next M lines will contain two integers ui,vi(1≤ui,vi≤N) — player ui tackled player vi. Each tackle between two players will be reported at most once.

Output:
Print the maximum possible number of Robots or Humans.

Examples:
Input:
5 6
3 4
3 2
5 4
5 2
4 1
1 2
Output:
3
Input:
5 4
4 3
1 3
3 2
3 5
Output:
4
Input:
4 1
1 3
Output:
3
Input:
6 6
1 3
1 4
3 6
4 6
4 5
6 2
Output:
3





C - The Knight of Königsberg
[Time limit per test1 second
memory limit per test256 megabytes]

You are given an N×N chessboard and the initial position (x1,y1) of a Knight piece. You need to find the minimum number of moves the Knight needs to reach the target position (x2,y2). If it is not possible to reach the target, print −1.

The Knight can move one step in any of the 8 possible directions as shown in the picture.

Input:
The first line contains an integer (1≤N≤2×103) — the size of the chessboard.
The second line contains four integers (1≤x1,y1,x2,y2≤N) — the initial position (x1,y1) and the target position (x2,y2) of the Knight on the chessboard.

Output:
Print the minimum number of moves the Knight needs to reach the target position. If it's not possible, print −1.

Examples:
Input:
3
1 2 1 3
Output:
3
InputCopy
3
1 1 2 2
Output:
-1
Input:
10
8 4 3 1
Output:
4





D - Easy Tree Queries
[Time limit per test1 second
memory limit per test1024 megabytes]

There is a tree with N nodes. The tree is rooted at a given node R.
You will be given Q queries. In each query, you are asked to find the size of the subtree of a given node X.

Input:
The first line contains two integers N, R(1≤N≤2×10^5,1≤R≤N) — the number of nodes and the root of the tree.
The next N−1 lines each contain two integers ui,vi(1≤ui,vi≤N) — representing an bidirectional edge between nodes ui and vi.
The next line contains an integer Q(1≤Q≤2×105) — the number of queries.
The next Q lines each contain a single integer X(1≤X≤N) — the node whose subtree size you need to compute.

Output:
For each query, print a single integer — the size of the subtree of node X.

Examples:
Input:
4 1
3 1
1 2
4 2
3
1
4
2
Output:
4
1
2
Input:
5 3
1 2
5 3
3 2
2 4
5
3
5
4
2
1
Output:
5
1
1
3
1
Input:
8 2
1 7
7 3
3 6
6 5
5 2
2 8
8 4
8
6
4
2
1
7
5
8
3
Output:
4
1
8
1
2
5
2
3
Input:
1 1
1
1
Output:
1





E - What's the Diameter?
[Time limit per test1 second
memory limit per test1024 megabytes]

You are given an undirected connected graph with N nodes and N−1 edges. Your task is to find two nodes such that the path between those two nodes is the longest possible in the graph.

Input:
The first line contains one integer N (2≤N≤200000) — the number of nodes.
The next N−1 lines will contain two integers ui, vi (1≤ui,vi≤N) — denoting there is a bidirectional road between ui and vi.

Output:
On the first line, print a single integer — the length of the longest path. On the second line, print two integers A and B — the nodes that form this longest path. If multiple pairs exist, you may print any one.

Examples:
Input:
5
5 1
1 4
4 2
3 2
Output:
4
3 5
Input:
5
1 2
5 3
3 2
2 4
Output:
3
5 1
Input:
8
1 7
7 3
3 6
6 5
5 2
2 8
8 4
Output:
7
4 1
Input:
7
7 5
5 6
6 1
1 3
3 4
4 2
Output:
6
7 2





F - An Ancient Ordering
[Time limit per test1 second
memory limit per test256 megabytes]

You have found an old dictionary containing N words. The words are stored in an order that is different from the regular Latin lexicographic order.

Your task is to determine the order of the alphabet that satisfies the lexicographic order of this dictionary. If there are multiple valid orders, print the lexicographically smallest one. For example, the sequence S1=′′d x i k′′ is lexicographically smaller than the sequence S2=′′d x p a k′′.

If no such valid sequence exists, print −1. A valid ordering is not possible if the characters create cyclic dependencies or if a longer word appears before a shorter word that is a prefix of it.

Input:
The first line contains an integer N(1≤N≤1000) — the number of words in the dictionary.
The next N line contains a string S (1≤|S|≤100). Each word consists of only lowercase Latin letters a−z.

Output:
Find out the order of the alphabets that satisfy the sorting order of the words in the given dictionary. If there are multiple valid orders, print the lexicographically smallest one. If no such valid sequence exists, print −1.

Examples:
Input:
3
eat
tea
ate
Output:
eta

Input:
9
error
tooth
tot
teeth
their
there
thi
tie
hit
Output:
oethir

Input:
6
gef
gie
hf
hd
hc
ha
Output:
efdcaghi

Input:
5
cmwaqe
yent
jtdgx
wlp
xufjpf
Output:
acdefglmnpqtuyjwx

Input:
6
abc
ab
p
pq
pqr
pqrs
Output:
-1

Input:
2
pigeon
pigeons
Output:
eginops

Input:
4
ab
bc
ca
ac
Output:
-1

----------------------------------------------------------LAB - 07----------------------------------------------------------------------

A - Shortest Path
[Time limit per test1 second
memory limit per test1024 megabytes]

You are given an directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
There is a source and a destination. Your task is to find the shortest distance from the source node to the destination node and print the path taken. If multiple shortest paths exist, print any one of them. If no such path exists, print −1.

Input:
The first line contains four integers N,M,S,D(2≤N≤2×10^5,1≤M≤3×10^5,1≤S,D≤N) — the number of vertices, total number of edges, source and destination.
The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.
The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is the other endpoint of the i-th edge.
The fourth line contains M integers w1,w2,w3…wm (1≤wi≤106) — where the i-th integer represents the weight of the i-th edge.
The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

Output:
If a valid path exists from S to D, print the shortest distance S to D on the first line.
On the second line, print the nodes in the path in order from S to D. If multiple shortest paths exist, print any one of them.
If no such path exists, print −1.

Examples:
Input:
4 3 4 2
1 3 4
2 2 3
3 4 5
Output:
9
4 3 2

Input:
6 5 1 5
1 4 1 6 4
2 1 6 2 6
3 3 4 3 4
Output:
-1

Input:
2 1 2 1
2
1
7
Output:
7
2 1

Input:
5 7 2 4
1 1 5 4 2 3 2
5 4 3 5 5 4 3
3 8 2 6 6 4 3
Output:
7
2 3 4





B - Where to Meet?
[Time limit per test2 seconds
memory limit per test1024 megabytes]

Alice and Bob are in a hurry to meet each other and have to traverse through a directed graph with weighted edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges. Alice starts from node S and Bob starts from node T. They want to find a common node in the graph where they can meet each other in the minimum amount of time. Alice or Bob can wait at any node if they want to.

Input:
The first line contains four integers N,M,S,T(2≤N≤2×105,1≤M≤3×105,1≤S,T≤N) — the number of vertices, the total number of edges, the starting node of Alice, and the starting node of Bob. The next M lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤106) — there is a edge from the node ui to the node vi with a weight wi.

Output:
Print two integers separated by a space: the minimum time required for Alice and Bob to meet, and the node where they meet. If there are multiple such nodes, print the smallest node. If no such node exists, print −1.

Examples:
Input:
5 5 1 5
1 2 1
2 3 1
5 3 2
1 4 2
5 4 2
Output:
2 3
Input:
6 5 1 5
1 2 3
4 1 3
1 6 4
6 2 3
4 6 4
Output:
-1
Input:
2 1 2 2
2 1 7
Output:
0 2
Input:
5 7 2 5
1 5 3
1 4 8
5 3 2
4 5 6
2 5 6
3 4 4
2 3 3
Output:
3 3





C - Minimize the Danger
[Time limit per test2 seconds
memory limit per test1024 megabytes]

You are in a city with N cities connected by M bi-directional roads. Each road has a danger level, where a higher number means the road is more dangerous.
You start in city 1 and need to go to every other city. The goal is to find the minimum danger level you would face to reach each city from city 1. The danger of a path is defined as the highest danger level of any road on that path.

For each city, find the minimum danger level of the path from city 1. If a city is not reachable from city 1, print −1. The danger of reaching city 1 is always 0.

Input:
The first line contains two integers N,M(2≤N≤2⋅10^5,1≤M≤3⋅10^5) — the number of cities, the total number of roads.

The next M lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤106) — node ui is connected to node vi with a weight wi.

Output:
Output n integers, where i-th integer represents the minimum danger level you'd have to face in order to go from city 1 to city i.

Examples:
Input:
4 3
2 1 3
2 3 5
3 4 3
Output:
0 3 5 5
Input:
6 5
1 2 3
1 4 5
1 6 2
2 6 3
4 6 1
Output:
0 3 -1 2 -1 2
Input:
2 1
2 1 5
Output:
0 5
Input:
5 7
1 5 3
1 4 2
5 3 1
5 4 6
5 2 5
3 4 4
3 2 8
Output:
0 5 3 2 3





D - Beautiful Path
[Time limit per test2 seconds
memory limit per test1024 megabytes]

You are given an directed graph with N nodes and M edges. The graph contains no self-loops or multiple edges. The edges have no weight. The nodes are numbered from 1 to N and have a weight. You need to find the cost of a path, if there is any, from node S to node D with the minimum cost. The cost of a path is the sum of the weights of the nodes in that path.

Input:
The first line contains four integers N,M,S,D(2≤N≤2×105,1≤M≤3×105,1≤S,D≤N) — the number of vertices, total number of edges, source, and destination.
In the next line, there will be N integers w1,w2,w3…wn (1≤wi≤10^6) separated by spaces – representing the weights of each node.
The next M lines will contain two integers ui,vi(1≤ui,vi≤N) — there is an edge from the node ui to the node vi.

Output:
If a valid path exists from S to D, print the minimum cost of the path. Otherwise, print −1.

Examples:
Input;
4 3 1 2
3 4 5 4
1 2
3 2
4 3
Output:
7
Input:
6 5 5 3
3 3 4 3 4 1
1 2
4 1
1 6
6 2
4 6
Output:
-1
Input:
2 1 1 1
7 6
2 1
Output:
7
Input:
5 7 3 5
3 8 2 6 6
1 5
1 4
5 3
4 5
2 5
3 4
2 3
Output:
14





E - Parity Edges
[Time limit per test1.5 seconds
memory limit per test1024 megabytes]

You are given a directed weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
Your task is to find the shortest distance from node 1 to node N, with an additional constraint: the path cannot contain two consecutive edges with the same parity (i.e., both even or both odd). If no such path exists, print −1.

Input:
The first line contains two integers N,M(2≤N≤2×10^5,1≤M≤3×10^5) — the number of vertices, total number of edges.
The second line contains M integers u1,u2,u3…um (1≤ui≤N) — where the i-th integer represents the node that is one endpoint of the i-th edge.
The third line contains M integers v1,v2,v3…vm (1≤vi≤N) — where the i-th integer represents the node that is the other endpoint of the i-th edge.
The fourth line contains M integers w1,w2,w3…wm (1≤wi≤106) — where the i-th integer represents the weight of the i-th edge.
The i-th edge of this graph is from the i-th node in the second line to the i-th node in the third line.

Output:
Print a single integer — the minimum distance from node 1 to node N following the given constraint. If there is no valid path, print -1.

Examples:
Input:
4 3
1 3 2
4 4 3
3 4 5
Output:
3
Input:
6 5
1 4 1 6 4
2 1 6 2 6
3 3 4 3 4
Output:
4
Input:
2 1
2
1
7
Output:
-1
Input:
5 7
1 1 4 5 2 3 2
4 5 3 4 4 5 3
3 8 2 6 6 4 3
Output:
8





F - Shortest Path Revisited
[Time limit per test3 seconds
memory limit per test1024 megabytes]

You are given a bidirectional weighted graph with N nodes and M edges. The nodes are numbered from 1 to N. The graph contains no self-loops or multiple edges.
There is a source and a destination. Your task is to find the cost of the second shortest path from the source node to the destination node. If no such path exists, print −1.
Note: Second shortest path will be strictly greater than the shortest path

Input:
The first line contains four integers N,M,S,D(2≤N≤2×105,1≤M≤3×105,1≤S,D≤N) — the number of vertices, total number of edges, source, and destination.
The next M lines will contain three integers ui,vi,wi(1≤ui,vi≤N,1≤wi≤106) — there is an edge between the node ui and the node vi with a weight wi.

Output:
If a valid path exists from S to D, print the cost of the second shortest path from S to D.
If no such path exists, print −1.

Examples
Input:
4 3 2 3
2 1 3
2 3 5
3 4 3
Output:
11

Input:
6 5 3 4
1 2 3
1 4 5
1 6 2
2 6 3
4 6 1
Output:
-1

Input:
2 1 2 2
2 1 5
Output:
10

Input:
5 7 2 5
1 5 3
1 4 2
5 3 1
5 4 6
5 2 5
3 4 4
3 2 8
Output:
7
