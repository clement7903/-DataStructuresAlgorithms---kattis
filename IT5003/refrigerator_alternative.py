from math import inf
pa, ka, pb, kb, n = list(map(int, input().split()))
opt_a, opt_b, opt_c = inf, inf, inf
for ta in range(n//ka+1):
  for tb in range(n//kb+1):
    if ta*ka + tb*kb >= n:
      if ta*pa + tb*pb < opt_c:
        opt_a, opt_b, opt_c = ta, tb, ta*ka + tb*kb

print(opt_a, opt_b, opt_c)