# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Reprak11

if __name__ == '__main__':
    s = input()
    print(True in [x.isalnum() for x in s])
    print(True in [x.isalpha() for x in s])
    print(True in [x.isdigit() for x in s])
    print(True in [x.islower() for x in s])
    print(True in [x.isupper() for x in s])