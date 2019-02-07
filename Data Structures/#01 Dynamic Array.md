## Dynamic Array

### Problem
  * Create a list, *seqList*, of *N* empty sequences, where each sequence is indexed from 0 to *N* - 1. 
The elements within each of the *N* sequences also use 0-indexing.
  * Create an integer, *lastAnswer*, and initialize it to 0.
  * The 2 types of queries that can be performed on your list of sequences *(seqList)* are described below:
  
  I. Query: 1 x y
  
    1. Find the sequnce, seq, at index ((x ⊕ lastAnswer) % N) in seqList.
    2. Append integer y to sequence seq.
        
  II. Query 2 x y
  
    1. Find the sequnce, seq, at index ((x ⊕ lastAnswer) % N) in seqList.
    2. Find the value of element y % size in seq(where size is the size of seq) and assign it to lastAnswer.
    3. Print the new value of lastAnswer on a new line. 
#### Task
Given *N*, *Q*, and *Q* queries, execute each query.                                                                                  
**Note:** ⊕ is the bitwise XOR operation, which corresponds to the ^ operator in most languages. 
Learn more about it on [Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or 'Exclusive or
').
#### Input Format
The first line contains two space-separated integers, *N* (the number of sequences) and *Q* (the number of queries), respectively. 
Each of the *Q* subsequent lines contains a query in the format defined above.
#### Constraints
  * 1 ≤ *N, Q* ≤ 10^5
  * 0 ≤ *x* ≤ 10^9
  * 0 ≤ *y* ≤ 10^9
  * It's guaranteed that query type 2 will never query an empty sequence or index.
#### Output Format
For each type 2 query, print the updated value of *lastAnswer* on a new line.
#### Sample Input 
```json
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
```
#### Sample Output 
```json
7
3
```
#### Explanation 
Initial Values:                                                                                                         
*N* = 2                                                                                                                 
*lastAnswer* = 0                                                                                                                        
*S(0)* = []                                                                                     
*S(1)* = []                                                                                                             

Query 0: Append 5 to sequence ( ( 0 ⊕ 0 ) % 2 ) = 0.                                                                                   
*last Answer* = 0                                                                                       
*S(0)* = [5]                                                                                                                    
*S(1)* = []                                                                                                     

Query 1: Append 7 to sequence ( ( 1 ⊕ 0 ) % 2 ) = 1.                                                                                
*last Answer* = 0                                                                                       
*S(0)* = [5]                                                                                                                    
*S(1)* = [7]                                                                                                     

Query 2: Append 3 to sequence ( ( 0 ⊕ 0 ) % 2 ) = 0.                                                                                    
*last Answer* = 0                                                                                       
*S(0)* = [5,3]                                                                                                                    
*S(1)* = [7]                                                                                                     

Query 3: Assign the value at index 0 of sequence ( ( 1 ⊕ 0 ) % 2 ) = 1 to *lastAnswer*, print *lastAnswer*.                             
*last Answer* = 7                                                                                       
*S(0)* = [5,3]                                                                                                                    
*S(1)* = [7]                                                                                                     
```json
7
```
Query 3: Assign the value at index 1 of sequence ( ( 1 ⊕ 7 ) % 2 ) = 0 to *lastAnswer*, print *lastAnswer*.                             
*last Answer* = 3                                                                                       
*S(0)* = [5,3]                                                                                                                    
*S(1)* = [7]                                                                                                         
```json
3
```
