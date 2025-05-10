# CSE221_Algorithms

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
