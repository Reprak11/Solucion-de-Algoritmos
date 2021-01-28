# https://codeforces.com/contest/731/problem/A
# Reprak11

word = [char for char in input()]
word = list(map(lambda x: ord(x),word))
word.insert(0,ord('a'))

rotations=0
for i in range(len(word)-1):
    a=word[i]-word[i+1]
    b=word[i+1]-word[i]
    a += 26 if a<0 else 0
    b += 26 if b<0 else 0
    rotations += a if a<b else b
print(rotations)
