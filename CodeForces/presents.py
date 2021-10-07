# https://codeforces.com/contest/136/problem/A
# Reprak11

n = int(input())
pi = list(map(int,input().split()))
i = []

for e in range(1,n+1):
    i.append(pi.index(e)+1)

print(" ".join(map(str,i)))
