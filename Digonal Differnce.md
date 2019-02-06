## Diagonal Differce

### Problem
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:
```json
1 2 3
4 5 6
9 8 9  
```
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17. Their absolute difference is |15-17| =2.
#### Function description
Complete the diagonalDiffernce function. It must return an integer representing the absolute diagonal difference.                     
diagonalDifference takes the following parameter:
  * arr: an array of integers.
#### Input Format
The first line contains a single integer, n, the number of rows and columns in the matrix arr.                        
Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
#### Constraints
  * -100 ≤ arr[i][j] ≤ 100
#### Out Format
Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
#### Sample Input
```json
3
11 2 4
4 5 6
10 8 -12
```
#### Sample Output
```json
15
```
#### Explanation

The primary diagonal is:
```json
11
   5
     -12
```
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
```json
     4
   5
10
```
Sum across the secondary diagonal: 4 + 5 + 10 = 19                          
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
### Solution
```json
arr = []
n = int(input())
sum1 = 0
sum2 = 0
q = n-1

for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    sum1 = sum1+ arr[i][i]
    sum2 = sum2 + arr[i][q]
    q -= 1
print(abs(sum1-sum2))
```
