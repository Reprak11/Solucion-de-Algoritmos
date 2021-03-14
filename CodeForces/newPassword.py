# https://codeforces.com/contest/770/problem/A
# Reprak11
import random

n, k = map(int, input().strip().split())

letters = []
letters.append(random.randint(97, 122))

while (len(letters) < k):
    char = random.randint(97, 122)
    if not(char in letters):
        letters.append(char)

password = ""
i = 0

while(len(password) < n):
    if i >= k:
        i = 0
    password += chr(letters[i])
    i += 1

print(password)


