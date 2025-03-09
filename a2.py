class student:
    grade = 11
    name = "Brian"

    def introduction(self):
        print("Hi, I am a Student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)

ob = student()
ob.introduction()
ob.details()