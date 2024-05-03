class StudySubject:
    name: str
    hours: int
    enable: bool

    def __init__(self, name: str, hours: int, enable: bool):
        self.name = name
        self.hours = hours
        self.enable = enable

    def info_study(self):
        print(f'Study: {self.name} | {self.hours}')


python = StudySubject(name=input(str('Name(subjects): ')), hours=input(str('Hours: ')), enable=True)


# python.info_study()

class Student:
    name: str
    surname: str
    study: list

    def __init__(self, name: str, surname: str, study: list):
        self.name = name
        self.surname = surname
        self.study = study

    def info_student(self):
        print(f'Student: {self.name} | {self.surname}')


student = Student(name=input(str('Name(student): ')), surname=input(str('Surname: ')), study=[python])



class Group:
    name: str
    number: list
    age: int
    student: list
    study: list

    def __init__(self, name: str, number: list, age: int, student: list, study: list):
        self.Name = name
        self.Number = number
        self.Age = age
        self.student = student
        self.study = study
    def info_Group(self):
        print(f'Group: {self.Name} | {self.Number} | {self.Age}')

    def info_all(self):
        self.info_Group()
        self.student.info_student()
        self.study.info_study()


group = Group(name=input(str('Name(group): ')), number=input(str('Number: ')), age=input(str('Age: ')), student=student,study=python)
group.info_all()

