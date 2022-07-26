class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        all_grades = []
        for cours in self.grades:
            all_grades.extend(self.grades[cours])
            self.avg_grades = round(sum(all_grades) / len(all_grades), 1)
        return (f'имя: {self.name}\n'  f'фамилия: {self.surname}\n' f'средняя оценка за дз: {self.avg_grades}\n'
    f'курсы в процессе обучения: {self.courses_in_progress}\n' f'завершенные курсы: {self.finished_courses}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('нет такого студента')
            return
        return self.avg_grades < other.avg_grades


    def average_score(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.cours_in_progress = []



    def __str__(self):
        all_grades = []
        for cours in self.grades:
            all_grades.extend(self.grades[cours])
            self.avg_grades = round(sum(all_grades) / len(all_grades), 1)
        return f'имя:{self.name}\n' f'фамилия:{self.surname}\n' f'средняя оценка за лекции:{self.avg_grades}'



    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('нет такого лектора')
            return
        return self.avg_grades < other.avg_grades



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'имя: {self.name}\n' f'фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

some_student = Student('Ruoy', 'Eman', ' ')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в програмирование']

best_student = Student('Ivan', 'Petrov', ' ')
best_student.finished_courses += ['Введение в програмирование']
best_student.courses_in_progress += ['Python', 'Git']


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

some_reviewer.rate_hw(best_student, 'Python', 8)
some_reviewer.rate_hw(best_student, 'Python', 9)

some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Git', 10)

some_reviewer.rate_hw(best_student, 'Git', 7)
some_reviewer.rate_hw(best_student, 'Git', 7)

some_lecturer = Lecturer('Some', 'Buddy')
best_lecturer = Lecturer('Ivan', 'Ivanov')

some_student.average_score(some_lecturer, 'Python', 8)
some_student.average_score(some_lecturer, 'Git', 9)

some_student.average_score(best_lecturer, 'Python', 7)
some_student.average_score(best_lecturer, 'Git', 8)


student = [some_student, best_student]
lecturer = [some_lecturer, best_lecturer]

def a_stud(student):
    all_grades = []
    for studen in student:
        for grade in studen.grades.values():
            all_grades.extend(grade)
        result = sum(all_grades) / len(all_grades)
        return result
students_a = a_stud(student)

def b_lect(lecturer):
    all_grades = []
    for lectur in lecturer:
        for grade in lectur.grades.values():
            all_grades.extend(grade)
        result = sum(all_grades) / len(all_grades)
        return result
lecturer_b = b_lect(lecturer)




print(some_student)
print()
print(some_reviewer)
print()
print(some_lecturer)
print()
print(best_lecturer)
print()
print(best_student)
print()
print(some_student > best_student)
print(some_lecturer > best_lecturer)
print()
print(f'средняя оценка студентов:{students_a}')
print(f'средняя оценка лекторов:{lecturer_b}')
