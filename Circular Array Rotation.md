## Circular Array Rotation

### Problem:
Джон Ватсон хочет проверить Шерлока Холмса. Он дал ему массив A0,A1 ... AN-1 . 
Выполнил некоторое преобразование массива, а затем задал Шерлоку Q вопросов. 
Шерлок чувствует, что преобразование, которое применил Джон, называется **циклический сдвиг вправо на K**. 
Циклический сдвиг вправо на 1 преобразует массив A(0),A(1) ... A(N-1) в A(N-1),A(0) ... A(N-2). Джон применил сдвиг на единицу K раз.

Помогите Шерлоку ответить на вопросы. 
Каждый вопрос описывается целым числом X, в ответ на вопрос Шерлок должен выписать элемент AX преобразованного массива.
#### Input Format
Первая строка содержит три целых числа, записанных через пробел, N, K и Q. 
Следующая строка содержит N целых чисел, записанных через пробел, - массив A. 
Каждая из следующих Q строк содержит целое число X - описание текущего вопроса.
#### Constraints 
  1. 1 ≤ N ≤ 105 
  2. 1 ≤ A[i] ≤ 105 
  3. 1 ≤ K ≤ 105 
  4. 1 ≤ Q ≤ 500 
  5. 0 ≤ X ≤ N-1
#### Output Format
Для каждого вопроса выведите соответствующий элемент преобразованного массива.
#### Sample Input
```json
3 2 3
1 2 3
0
1
2
```
#### Sample Output
```json
2
3
1
```
#### Explanation
After the first rotation, the array becomes [3,1,2]. 
After the second (and final) rotation, the array becomes [2,3,1].

Let's refer to the array's final state as array *b* = [2,3,1]. For each query, we just have to print the value of b(m) on a new line:
  1. *m* = 0, *b(0)* = 2.
  2. *m* = 1, *b(1)* = 3.
  3. *m* = 2, *b(2)* = 1.
### Solution 
```json
N, K, Q = list(map(int, input().strip().split()))
A = list(map(int, input().strip().split()))
result = []
for q in range(Q):
    q = int(input())
    result.append(A[q-K % N])
for i in result:
    print(i)

```
