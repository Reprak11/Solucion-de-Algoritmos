# https://codeforces.com/contest/9/problem/A
# Reprak11
from fractions import Fraction

a = list(map(int, input().strip().split()))

rs=(6-max(a)+1)/6

print('1/1' if rs == 1 else Fraction(rs).limit_denominator())