"""
In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:
4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""

def exp_sum_answer(n):
  if n < 0:
    return 0
  dp = [1]+[0]*n
  for num in xrange(1,n+1):
    for i in xrange(num,n+1):
      dp[i] += dp[i-num]
  return dp[-1]
