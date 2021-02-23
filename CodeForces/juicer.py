# http://codeforces.com/contest/709/problem/A
# Reprak11

n, b, d = map(int, input().strip().split())
counter = 0
oranges = 0
a = map(int, input().strip().split())
for i in a:
    if i<=b:
        oranges += i
        if oranges > d:
            counter += 1
            oranges = 0
print(counter)