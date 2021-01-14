# https://codeforces.com/contest/677/problem/A
# Reprak11



n, h = map(int, input().strip().split())
friends = list(map(int, input().strip().split()))

output=0

for i in range(n):
    if friends[i] > h:
        output = output + 2
    else:
        output = output + 1

print(output)