student_score = [145, 22, 189, 3, 108, 79, 200, 59, 132, 15, 167, 97, 178, 34, 194, 48, 119, 156, 66, 88]

max_score = student_score[0]

for score in student_score:
    if max_score < score:
        max_score = score
print(max_score)
print(max(student_score))