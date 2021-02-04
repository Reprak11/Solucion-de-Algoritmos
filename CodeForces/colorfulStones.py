# https://codeforces.com/contest/265/problem/A
# Reprak11

s = list(input())
t = list(input())

l=1
for i in t:
    l += 1 if i == s[l-1] else 0

print (l)