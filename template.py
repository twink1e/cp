t = int(input()) # read a line with a single integer
for tc in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(tc, n + m, n * m))

list(filter(lambda x: x%2 != 0, numbers))
list(map(lambda x: x*2, numbers))
map(lambda (i,x): {'name':x, 'rank':i}, enumerate(ranked_users))

from functools import reduce

sumOfNumbers = reduce(lambda x,y: x+y, numbers)