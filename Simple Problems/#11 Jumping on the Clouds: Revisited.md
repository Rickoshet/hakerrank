## Jumping on the Clouds: Revisited

### Problem
Aerith is playing a cloud hopping game. 
In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. 
Her character must jump from cloud to cloud until it reaches the start again.

To play, Aerith is given an array of clouds, *c* and an energy level *e* = 100.
She starts from *c*[0] and uses 1 unit of energy to make a jump of size *k* to cloud *c*[*(i+k) % n*]. 
If Aerith lands on a thundercloud, *c*[*i*] = 1, her energy *(e)* decreases by 2 additional units.
The game ends when Aerith lands back on cloud 0.

Given the values of *n*, *k*, and the configuration of the clouds as an array *c*, 
can you determine the final value of *e* after the game ends?

For example, give *c* = [0,0,1,0] and *k* = 2, the indices of her path are 0 → 2 → 0. Her energy level reduces by 1 for each jump to 98. 
She landed on one thunderhead at an additional cost of 2 energy units. Her final energy level is 96.

**Note:** Recall that *%* refers to the [modulo operation](https://en.wikipedia.org/wiki/Modulo_operation 'Modulo Operation'). 
In this case, it serves to make the route circular. 
If Aerith is at *c*[*n* -1] and jumps 1, she will arrive at *c*[0].

#### Function description
Complete the jumpingOnClouds function. 
It should return an integer representing the energy level remaining after the game.

jumpingOnClouds has the following parameter(s):
  * c: an array of integers representing cloud types
  * k: an integer representing the length of one jump
#### Input Format
The first line contains two space-separated integers, *n* and *k*, the number of clouds and the jump distance. 
The second line contains *n* space-separated integers *c*[*i*] where 0 ≤ *i* < *n*. Each cloud is described as follows:
  * If *c*[*i*] = 0, then cloud *i* is a cumulus cloud.
  * If *c*[*i*] = 1, then cloud *i* is a thunderhead.
#### Constraints
  * 2 ≤ *n* ≤ 25
  * 1 ≤ *k* ≤ n
  * *n % k = 0*
  * *c*[*i*] ∈ {0,1}
#### Output Format
Print the final value of *e* on a new line.
#### Sample Input
```json
8 2
0 0 1 0 0 1 1 0
```
#### Sample Output
```json
92
```
#### Explanation

In the diagram below, red clouds are thunderheads and purple clouds are cumulus clouds:
![alt text](https://s3.amazonaws.com/hr-challenge-images/0/1462454878-26f414ec0f-may4.png)                                              
Observe that our thunderheads are the clouds numbered , , and . Aerith makes the following sequence of moves:
  1. Move: 0 → 2, Energy: *e* = 100 - 1 - 2 = 97
  2. Move: 2 → 4, Energy: *e* = 97 - 1 = 96
  3. Move: 4 → 6, Energy: *e* = 96 - 1 - 2 = 93
  4. Move: 6 → 0, Energy: *e* = 93 - 1 = 92
### Solution
```py
n, k  = map(int, input().strip().split())
clouds = list(map(int, input().strip().split()))
print(100 - sum(1 + 2 * clouds[i] for i in range(0, n, k)))
```
