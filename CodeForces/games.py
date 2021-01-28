# https://codeforces.com/contest/268/problem/A
# Reprak11

n = int(input())
uniform = []
for i in range(n):
    uniform.append(list(map(int, input().strip().split())))


guestUniform = 0
for i in range(n):
    for j in range(n):
        if uniform[i][0] == uniform[j][1]:
            guestUniform += 1
print(guestUniform)