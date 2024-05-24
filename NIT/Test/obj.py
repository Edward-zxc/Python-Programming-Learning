class Person:
    # （1）初始化三个示例变量，其中gender为私有
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def detail(self):
        print("姓名:", self.name)
        print("年龄:", self.age)
        print("性别:", self.__gender)

    def get_gender(self):
        return self.__gender


class Student(Person):
    def __init__(self, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.grade = grade

    def detail(self):
        super().detail()
        print("年级:", self.grade)


person1 = Person("张三", 25, "男")

person1.detail()
print("性别:", person1.get_gender())
print()

student1 = Student("李四", 20, "女", "大一")

student1.detail()
