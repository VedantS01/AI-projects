A cute Spider of weight W has created a web which a circle made up of L layers. The web is made of concentric L circles. Now the spider wants to move around the web and needs your help. The spider can stay on the web (on centre or on any layer) as long its weight W is less than or equal to the strength of the current position.

Whenever this cute spider creates a web, it ensures its centre has a strength of M and after every layer the strength goes on decreasing by 1 i.e. if centre's M = 12 then first layer will have strength 11, second layer will have strength 10 and the last layer will have strength of M-L.

Now you know that spider is on Xth layer and wants to go on Yth layer, can you tell us if this cute Spider can jump or fall?

# Input

The first line has t (1 <= t <= 1000) denoting the number of test cases

Each line of test case has 5 integers W, L, M, X, Y (0 <= W, L <= M <= 10000, 0 <= X, Y <= L)

# Output

Output the string JUMP indicating if Spider can jump or FALL if Spider cannot jump in all uppercase

# Sample 1

## Input

3

10 8 12 2 5

12 8 20 2 5

11 8 12 2 5 

## Output

FALL

JUMP

FALL

## Explanation

Spider cannot jump as 5th layer has a strength of 7

Spider can jump as 5th layer has a strength of 15 which is greater than 12

Spider will fall from the web when he is on 2nd layer as it has a strength of 10.