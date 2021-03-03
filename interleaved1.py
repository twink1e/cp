t = int(input()) # read a line with a single integer
for tc in range(1, t + 1):
  s = input()
  # IO Io iO io
  print("IO Io iO io")
  cr = [0,0,0,0]
  ans = 0
  for c in s:
    if c == 'I':
      if cr[0] == 0:
        cr[0] = 1
      else:
        cr[1] = 1
    elif c == 'i':
      if cr[2] == 0:
        cr[2] = 1
      else:
        cr[3] = 1
    elif c == 'o':
      if cr[3] == 1:
        cr[3] = 0
      else:
        cr[1] = 0
    else:
      if cr[0] == 1:
        cr[0] = 0
        ans += 1
      else:
        cr[2] = 0
    print(c, cr)
  print("Case #{}: {}".format(tc, ans))