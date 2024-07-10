class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def display(self):
        print("姓名:", self.name)
        print("年龄:", self.age)
        print("性别:", self.__gender)

class Student(Person):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def display(self):
        super().display()
        print("年级:", self.grade)



person1 = Person("张三", 25, "男")

person1.display()
print()


student1 = Student("李四", 20, "女", "大一")

student1.display()
