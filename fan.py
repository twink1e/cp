t = int(input()) # read a line with a single integer
for tt in range(1, t + 1):
  x, y, m = input().split(' ')
  x = int(x)
  y = -int(y)
  ans = False
  for i in range(len(m)):
  	if m[i] == 'S':
  		y += 1
  	elif m[i] == 'N':
  		y -= 1
  	elif m[i] == 'E':
  		x += 1
  	else:
  		x -= 1
  	if i+1 >= abs(x)+abs(y):
  		print("Case #{}: {}".format(tt, i+1))
  		ans = True
  		break
  if not ans:
  	print("Case #{}: IMPOSSIBLE".format(tt))