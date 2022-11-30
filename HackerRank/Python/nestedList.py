# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Reprak11

if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    
    second_lowest = (sorted(set(scores))[1])
    students = [name[0] for name in records if name[1] == second_lowest]
    
    for student in sorted(students):
        print(student)