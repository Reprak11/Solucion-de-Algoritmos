# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Reprak11

def print_formatted(number):
    # your code goes here
    space = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(space), '{0:o}'.format(i).rjust(space), '{0:x}'.format(i).upper().rjust(space), '{0:b}'.format(i).rjust(space))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)