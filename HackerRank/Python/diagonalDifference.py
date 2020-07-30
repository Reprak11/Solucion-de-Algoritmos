# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Reprak11

def diagonalDifference(arr):
    valor1 = 0
    valor2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i == j):
                valor1 += arr[i][j]
            if(len(arr)-1 == j+i ):
                valor2 += arr[i][j]
    return abs(valor1 - valor2)

def diagonalDifference2(arr):
    valor1 = 0
    valor2 = 0
    for i in range(len(arr)):
        valor1 += (arr[i][i])
        valor2 += (arr[i][len(arr)-i-1])   
    return abs(valor1 - valor2)



if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(diagonalDifference2(arr))