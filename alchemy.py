t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  s = input()
  a = 0
  b = 0
  for c in s:
  	if c == 'A':
  		a += 1
  	else:
  		b += 1
  print("Case #{}: {}".format(i, 'N' if abs(a-b) > 1 else 'Y'))