t = int(input()) # read a line with a single integer
for tc in range(1, t + 1):
	n = int(input())
	rec = {}
	start = {}
	ans = 0
	ins = []
	for _ in range(n):
		p, h = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
		ins.append((p-h, p+h, p, h))
	ins.sort()

	for (_, _, p, h) in ins:
		rec[p+h] = max(rec[p+h] if p+h in rec else h, (rec[p] if p in rec else 0) + h)
		rec[p] = max(rec[p] if p in rec else h, (rec[p-h] if p-h in rec else 0) + h)
		start[p-h] = max(start[p-h] if p-h in start else h, (start[p] if p in start else 0) + h)
		start[p] = max(start[p] if p in start else h, (start[p+h] if p+h in start else 0) + h)
		# print(rec)
		ans = max(ans, rec[p], rec[p+h], start[p], start[p-h])

	print("Case #{}: {}".format(tc, ans))