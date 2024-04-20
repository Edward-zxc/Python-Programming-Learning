# 创建学生选课字典
student_courses = {
    'Alice': ['Math', 'Physics', 'Chemistry'],
    'Bob': ['English', 'History', 'Biology']
}

# 输出每个学生姓名及选课信息
for student, courses in student_courses.items():
    print(f"{student} 选修的课程有：{', '.join(courses)}")
