# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Reprak11

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        count += string[i:].startswith(sub_string)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)