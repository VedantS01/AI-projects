# Problem

Given a city of n houses. Initially ith house has a color c[i]. On the festival of Holi, the city will look more beautiful with more colors. Now u can choose a house and change its color to a color a where x <= a <= y. This operation can be performed at most k times. Find max number of different colored houses you can achieve to make the city most colorful after performing all the operations optimally.

# Input Format

First line contains an integer T - the number of test cases.

First line of each test case contains 4 space separated integers n, x, y, k as mentioned in the statement.

Next line of the test case contains n space separated integers c[1], c[2], ..., c[n] - initial colors of the houses.

# Constraints

1 <= T <= 10^5

1 <= n <= 10^5

0 <= c[i] <= 10^9

0 <= x <= y <= 10^9

0 <= k <= n

Sum of n over all test cases wont exceed 5*10^5

# Output Format

For each test case, print maximum possible number of different colored houses in the city in a newline.

# Sample I/O

## Input

3

3 1 2 2

3 3 3

5 2 3 3

1 2 3 3 7

6 1 4 1

3 4 5 5 5 5

## Output

3

4

4

## Explanation

In first case, change the color of second and third house to 1 and 2 respectively. Hence total 3 different colors.

In second case, two houses has same color 3 but we cant change it to a new color. The new assigned color would be either 2 or 3, in both cases, it doesn't increase number of colors.

In third case, change the color of 4th house to 1. We can't change colors of other houses now as we had only 1 operation.