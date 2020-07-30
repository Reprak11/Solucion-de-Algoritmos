# https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen
# Reprak11

def compareTriplets (a , b):
    puntos = [0, 0]
    for i in range (len(a)):
        if a[i] > b [i]:
            puntos[0] += 1
        elif a[i] < b[i]:
            puntos[1] += 1
    return puntos


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)