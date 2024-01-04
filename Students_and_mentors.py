# Класс BaseMethod включает повторяющиеся методы (вычисление среднего значения оценок и их сравнение)
# Данный класс будет родительским по отношению к классам Student и Lecturer
class BaseMethod:
    def avg(self):
        average = []
        for i in self.grades.values():
            for j in i:
                average.append(j)
        self.avg_grades = round((sum(average) / len(average)), 2)
        return self.avg_grades

    def __lt__(self, other):
        if ((isinstance(self, Student)==isinstance(other, Student))==True) or ((isinstance(self, Lecturer)==isinstance(other, Lecturer))==True):
            return self.avg() < other.avg()
        else:
            return None

    def __le__(self, other):
        if ((isinstance(self, Student)==isinstance(other, Student))==True) or ((isinstance(self, Lecturer)==isinstance(other, Lecturer))==True):
            return self.avg() <= other.avg()
        else:
            return None

    def __eq__(self, other):
        if ((isinstance(self, Student)==isinstance(other, Student))==True) or ((isinstance(self, Lecturer)==isinstance(other, Lecturer))==True):
            return self.avg() == other.avg()
        else:
            return None

    def __ne__(self, other):
        if ((isinstance(self, Student)==isinstance(other, Student))==True) or ((isinstance(self, Lecturer)==isinstance(other, Lecturer))==True):
            return self.avg() != other.avg()
        else:
            return None

# Класс Student (студенты)
class Student (BaseMethod):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grades = 0

    # Оценка работы лекторов
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 < grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Выведение основной информации о студенте
    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.avg_grades}\n'
               f'Курсы в процессе изучения: 'f'{", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return res

# Класс Mentor (преподаватели - лекторы и эксперты)
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс Lecturer (лекторы)
class Lecturer(Mentor, BaseMethod):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grades = 0

    # Выведение основной информации о лекторе
    def __str__(self):
        self.avg()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.avg_grades}')
        return res

# Класс Reviewer (эксперты)
class Reviewer(Mentor):
    # Оценка работы студентов
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Выведение основной информации об эксперте
    def __str__(self):
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}')
        return res

# Функция для выведения среднего значения по оценкам в рамках конкретного курса
# people_list - список конкретных групп людей, оцениваемых в рамках курса (студенты/лекторы)
# course_name - название курса, в рамках которого оцениваются студенты/лекторы
def get_result(people_list, course_name):
    list_of_grades = []
    for s in people_list:
        if course_name in s.grades.keys():
            for v in s.grades[course_name]:
                list_of_grades.append(v)
        else:
            continue
    if len(list_of_grades) > 0:
        mean_value = round((sum(list_of_grades) / len(list_of_grades)), 2)
        print(f'Средний балл по курсу {course_name}: {mean_value}')
        return mean_value
    else:
        print('Данные по оценкам отсутствуют')

# Функция для выведения среднего балла для студентов в рамках курса
def get_avg_student_grades(student_list, course_name):
    correct_student_list = []
    for s in student_list:
        if isinstance(s, Student) == True:
            correct_student_list.append(s)
        else:
            print(f'Неверно заполнен следующий участник курса {course_name}:')
            print(s)
            break
    if len(correct_student_list) == len(student_list):
        return get_result(correct_student_list, course_name)

# Функция для выведения  среднего балла для лекторов в рамках курса
def get_avg_lecturer_grades(lecturer_list, course_name):
    correct_lecturer_list = []
    for l in lecturer_list:
        if isinstance(l, Lecturer) == True:
            correct_lecturer_list.append(l)
        else:
            print(f'Неверно заполнен следующий участник курса {course_name}:')
            print(l)
            break
    if len(correct_lecturer_list) == len(lecturer_list):
        return get_result(correct_lecturer_list, course_name)

# Создание студента №1
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

# Создание студента №2
other_student = Student('Bob', 'Dylan', 'man')
other_student.courses_in_progress += ['Python', 'Git']
other_student.finished_courses += ['Введение в программирование']

# Создание проверяющего №1
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

# Создание проверяющего №2
other_reviewer  = Reviewer('Some', 'Buddy')
other_reviewer.courses_attached += ['Python']
other_reviewer.courses_attached += ['Git']

# Создание лектора №1
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

# Создание лектора №2
other_lecturer = Lecturer('Some', 'Buddy')
other_lecturer.courses_attached += ['Python']
other_lecturer.courses_attached += ['Git']

print('*****Результат проверки работы функций добавления оценок*****')
# Выставление оценок студенту №1
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Git', 7)
print(f'Оценки студента 1: {some_student.grades}')

# Выставление оценок студенту №2
some_reviewer.rate_hw(other_student, 'Python', 8)
some_reviewer.rate_hw(other_student, 'Python', 10)
some_reviewer.rate_hw(other_student, 'Git', 7)
print(f'Оценки студента 2: {other_student.grades}')

# Выставление оценок лектору №1
some_student.rate_lec(some_lecturer, 'Python', 5)
some_student.rate_lec(some_lecturer, 'Python', 8)
some_student.rate_lec(some_lecturer, 'Git', 4)
print(f'Оценки лектора 1: {some_lecturer.grades}')

# Выставление оценок лектору №2
some_student.rate_lec(other_lecturer, 'Python', 6)
some_student.rate_lec(other_lecturer, 'Python', 9)
some_student.rate_lec(other_lecturer, 'Git', 4)
print(f'Оценки лектора 2: {other_lecturer.grades}')
print()

print('*****Проверка вывода функции печати для классов******')
print('***ПРОВЕРЯЮЩИЙ***')
print(some_reviewer)
print()
print('***ЛЕКТОР***')
print(some_lecturer)
print()
print('***СТУДЕНТ***')
print(some_student)
print()

print('*****Результат проверки работы функции рассчета среднего балла всех студентов по определенному курсу*****')
get_avg_student_grades([some_student, other_student], 'Python')
print()

print('*****Результат проверки работы функции рассчета среднего балла всех лекторов по определенному курсу*****')
get_avg_lecturer_grades([some_lecturer, other_lecturer], 'Python')
print()

print('*****Проверка функций сравнения*****')
print('***Студенты - больше равно/меньше равно***')
print(some_student >= other_student)
print(some_student <= other_student)
print(some_student >= other_lecturer)
print(some_lecturer <= other_student)
print()
print('***Студенты - больше/меньше***')
print(some_student > other_student)
print(some_student < other_student)
print(some_student < other_lecturer)
print(some_lecturer < other_student)
print()
print('***Студенты - равно/не равно***')
print(some_student == other_student)
print(some_student != other_student)
print(some_student == other_lecturer)
print(some_lecturer != other_student)
print()

print('***Лекторы - больше равно/меньше равно***')
print(some_lecturer >= other_lecturer)
print(some_lecturer <= other_lecturer)
print(some_lecturer >= other_student)
print(some_student <= other_lecturer)
print()
print('***Лекторы - больше/меньше***')
print(some_lecturer > other_lecturer)
print(some_lecturer < other_lecturer)
print(some_lecturer < other_student)
print(some_student < other_lecturer)
print()
print('***Лекторы - равно/не равно***')
print(some_lecturer == other_lecturer)
print(some_lecturer != other_lecturer)
print(some_lecturer == other_student)
print(some_student != other_lecturer)
print()