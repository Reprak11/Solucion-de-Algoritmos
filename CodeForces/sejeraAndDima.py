# https://codeforces.com/contest/381/problem/A
# Reprak11
n=int(input())
cards = list(map(int,input().split(" ")))

s=0
d=0

for i in range (n):
    if (i%2==0):
        s += cards.pop(0) if cards[0] >= cards[len(cards)-1] else cards.pop(len(cards)-1)
    else:
        d += cards.pop(0) if cards[0] >= cards[len(cards)-1] else cards.pop(len(cards)-1)

print(s,d)
