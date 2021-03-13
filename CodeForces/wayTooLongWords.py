# http://codeforces.com/contest/71/problem/A
# Reprak11

n = int(input())

for i in range(n):
    word = input()
    print(word[0]+str(len(word)-2)+word[len(word)-1]) if len(word) > 10 else print(word)