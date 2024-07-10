class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def detail(self):
        print("姓名:",self.name)
        print("年龄:",self.age)
        print("性别:",self.__gender)

class student(person):
    def __init__(self,name,age,gender,grade):
        super().__init__(name,age,gender)
        self.grade = grade
    def detail(self):
        super().detail()
        print("年级：",self.grade)


###实例化
person1 = person("sas",12,"nan")
person1.detail()
print() 


student1 = student("asa",12,"ann","dfsdf")
student1.detail()