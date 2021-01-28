# https://codeforces.com/contest/427/problem/A
# Reprak11

n = int(input())
events = list(map(int, input().strip().split()))

recruits = 0
untreated = 0
for i in events:
    if i == -1:
        if recruits == 0:
            untreated += 1
        else:
            recruits -= 1
    else:
        recruits += i
print(untreated)