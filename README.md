# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»

За основу выполнения [текущего домашнего задания](https://github.com/netology-code/py-homeworks-basic/tree/master/6.classes) был взят [код из предыдущего задания](https://github.com/netology-code/py-homeworks-basic/blob/master/6.classes/students_and_mentor.py). Решение домашнего задания приведено в файле Students_and_mentors.py.

## Задание № 1. Наследование
Классы Lecturer (лекторы) и Reviewer (эксперты) созданы. Их наследование с родительским классом Mentor работает должным образом.

## Задание № 2. Атрибуты и взаимодействие классов
Алгоритм методики оценки работы студентов проверяющими и лекторов студентами добавлен. Он учтен в методах rate_lec и rate_hw, содержащихся в классах Student (студенты) и Reviewer (эксперты). Атрибут-словарь, включающий список оценок студентов по конкретному курсу, сформирован в классе Lecturer (лекторы).

## Задание № 3. Полиморфизм и магические методы
Магический метод ```__str__``` построен. Он находится внутри классов Student (студенты), Lecturer (лекторы) и Reviewer (эксперты).

Методы выведения и сравнения среднего балла студентов/лекторов в рамках всех курсов были сформированы в классе BaseMethod, являющимся родительским по отношению к классам Student (студенты) и Lecturer (лекторы). Данный прием наследования классов был реализован для получения более компактного кода.

Результат выполнения задания № 3 - выведение основной информации об участниках курса и сравнение среднего балла студентов/лекторов работают исправно.

```python
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
```

## Задание № 4. Полевые испытания
Два экземпляра всех имеющихся классов созданы. Все созданные методы вызваны. Функции для подсчета средней оценки всех студентов/лекторов за ДЗ/лекции реализованы (get_avg_student_grades и get_avg_lecturer_grades).

Результат работы кода проверен в разрезе: 1) функций добавления оценок; 2) функции печати результатов классов; 3) функций рассчета среднего балла всех студентов и среднего балла всех лекторов по определенному курсу; 4) проверки функций сравнения общих средних баллов студентов/лекторов в разрезе операций "больше равно/меньше равно", "больше/меньше", "равно/не равно".
