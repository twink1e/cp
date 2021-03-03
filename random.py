t = int(input()) # read a line with a single integer
for tt in range(1, t + 1):
	u = int(input())
	al = set()
	rec = [[-1] for _ in range(11)]
	first = set()
	for _ in range(10**4):
  		n, m = input().split(" ")
  		for c in m:
  			al.add(c)
  		n = int(n)
  		if n < 10 and n >= 0:
  			rec[n].append(m)
  		if len(m) > 1:
  			first.add(m[0])


	ans=[-1] * 10

	for i in range(10):
		for c in rec[i]:
			if c in al:
				ans[i] = c
				al.discard(c)
				break
	if ans[0] == -1:
		for c in al:
			if c not in first:
				ans[0] = c
				al.discard(c)
				break
	for i in range(10):
		if ans[i] == -1:
			ans[i] = al.pop()
	print("Case #{}: {}".format(tt, ''.join(ans)))