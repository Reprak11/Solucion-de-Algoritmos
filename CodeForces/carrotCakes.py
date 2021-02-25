# http://codeforces.com/contest/799/problem/A
# Reprak11
import math
n, t, k, d = map(int, input().strip().split())

rondas = (math.ceil(n/k))

t1 = rondas * t
t2 = d + t

print(t1,t2)
print('YES' if t1 > t2 else 'NO')

