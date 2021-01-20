# https://codeforces.com/contest/405/problem/A
# Reprak11

n = int(input())
pichula = list(map(int, input().strip().split()))

#for tula in range(len(pichula)):
#    for tulaa in range(len(pichula)-tula-1):
#        if(pichula[len(pichula)-1-tula] < pichula[len(pichula)-tulaa-tula-2]):
#            diff = abs(pichula[len(pichula)-1-tula] - pichula[len(pichula)-tulaa-tula-2])
#            pichula[len(pichula)-1-tula] += diff
#            pichula[len(pichula)-tulaa-tula-2] -= diff

pichula = sorted(pichula)

print(' '.join(str(e) for e in pichula))