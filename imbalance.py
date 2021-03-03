t = int(input()) # read a line with a single integer
for tc in range(1, t + 1):
  n = int(input())
  remove = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  graph = {}
  for i in range(1, n+1, 2):
    graph[i] = [i+1]
    graph[i+1] = i
  print(graph)
  # print("Case #{}: {} {}".format(tc, n + m, n * m))