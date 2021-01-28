# https://codeforces.com/contest/266/problem/A
# Reprak11

n = int(input())
s = input()

cuenta = 0
pos = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        cuenta += 1

print(cuenta)