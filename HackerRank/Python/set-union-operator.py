# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Reprak11

n1 = int(input())
total_students_english = set(input().split())

n2 = int(input())
total_students_french = set(input().split())

print(len(total_students_english.union(total_students_french)))