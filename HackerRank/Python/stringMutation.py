# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Reprak11
def mutate_string(string, position, character):
    return string[0:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)