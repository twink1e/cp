t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
	n = int(input())
	inn = input()
	out = input()
	ans = [['Y'] * n for _ in range(n)]
	for j in range(n):
		if inn[j] == 'N':
			if j-1 >= 0:
				ans[j-1][j] = 'N'
			if j+1 < n:
				ans[j+1][j] = 'N'
		if out[j] == 'N':
			if j-1 >= 0:
				ans[j][j-1] = 'N'
			if j+1 < n:
				ans[j][j+1] = 'N'
	for j in range(n-2):
		fail = ans[j][j+1] == 'N'
		for k in range(j+2, n):
			if fail:
				ans[j][k] = 'N'
			elif ans[k-1][k] == 'N':
				fail = True
				ans[j][k] = 'N'
	# print(ans)
	for j in range(2, n):
		fail = ans[j][j-1] == 'N'
		for k in range(j-2, -1, -1):
			if fail:
				ans[j][k] = 'N'
			elif ans[k+1][k] == 'N':
				fail = True
				ans[j][k] = 'N'
	print("Case #{}:".format(i))
	for a in ans:
		print("".join(a))