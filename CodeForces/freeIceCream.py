# https://codeforces.com/contest/686/problem/A
# Reprak11

n, x = map(int, input().strip().split())
distress = 0

for i in range(n):
    operation, carries =  input().strip().split()
    if operation == '+':
        x += int(carries)
    else:
        if int(carries) > x:
            distress += 1
        else:
            x -= int(carries)

print(x, distress)