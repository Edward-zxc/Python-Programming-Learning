def average_score(scores):
    return round(sum(scores[1:]) / (len(scores) - 1))

def highest_score(student_scores):
    highest = max(student_scores, key=lambda x: sum(x[1:]))
    return highest[0], sum(highest[1:])

# 示例
student_scores = [
    ['Jack', 90, 89, 89],
    ['张三', 93, 82, 91],
    ['李四', 97, 86, 79],
    ['王五', 89, 81, 90],
    ['Helen', 77, 85, 85]
]

average_scores = {student[0]: average_score(student) for student in student_scores}
print("每个学生的平均成绩：", average_scores)

highest_student, total_score = highest_score(student_scores)
print("总成绩最高的学生：", highest_student)
print("他的总分：", total_score)
