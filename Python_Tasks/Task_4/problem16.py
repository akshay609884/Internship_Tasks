#  16 Nested Lists
# Hacker Rank Link: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    scores = set()
    
    # 1. Read total number of students
    n = int(input())
    
    # 2. Read name and score sequentially
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
        
    # 3. Sort unique scores to isolate the second lowest
    sorted_scores = sorted(list(scores))
    second_lowest_grade = sorted_scores[1]
    
    # 4. Filter students who share the second lowest grade
    result_names = [student[0] for student in students if student[1] == second_lowest_grade]
    
    # 5. Sort names alphabetically and print
    for name in sorted(result_names):
        print(name)



