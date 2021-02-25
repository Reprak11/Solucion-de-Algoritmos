# https://codeforces.com/contest/443/problem/A
# Reprak11

letters = len(''.join(list(set([x.strip() for x in input()[1:-1].split(',')]))))
print(letters)