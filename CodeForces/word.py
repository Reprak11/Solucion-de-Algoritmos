# https://codeforces.com/contest/59/problem/A
# Reprak11

n=input()

low=0
up=0

for i in n:
    if i.isupper():
        up += 1
    else:
        low += 1

print(n.upper() if up>low else n.lower())