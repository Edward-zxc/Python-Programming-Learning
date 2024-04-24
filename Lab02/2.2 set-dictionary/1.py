
student_courses = {
    'Alice': ['Math', 'Physics', 'Chemistry'],
    'Bob': ['English', 'History', 'Biology']
}

for student, courses in student_courses.items():
    print(f"{student} 选修的课程有：{', '.join(courses)}")
