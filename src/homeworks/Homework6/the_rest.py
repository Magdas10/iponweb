import date_and_time


class MoneyError(Exception):
    pass


class Money:
    exchange = {"AMD": 1, "RUB": 0.177391, "USD": 0.002495, "EUR": 0.002291}

    def __init__(self, amount: int, currency: str):
        if isinstance(amount, (int, float)) and amount >= 0 and isinstance(currency, str):
            self.__amount = amount
            self.__currency = currency
        else:
            raise MoneyError

    def __repr__(self):
        return str(self.__amount) + " " + self.__currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__amount = value
        else:
            raise MoneyError(f"Amount can't be negative {value}")

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value in Money.exchange.keys():
            self.__currency = value
        else:
            raise MoneyError(f"There is no such currency {value}")

    def conversation(self, new_curr: str):
        curr = self.currency
        self.currency = new_curr
        self.amount = (self.amount / Money.exchange[curr]) * Money.exchange[self.currency]
        return self

    def __add__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount += x.amount

    def __sub__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount -= x.amount

    def __truediv__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount /= x.amount

    def __eq__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount == x.amount

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount < x.amount

    def __gt__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount > x.amount

    def __le__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount <= x.amount

    def __ge__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount >= x.amount


# money1 = Money(150, "RUB")
# money2 = Money(800, "USD")
# money3 = Money(150, "RUB")
# # money3.amount = -123
# money2.conversation("RUB")
# print(money1)
# print(money2)
# # print(money2 >= money1)
# print(money1 >= money3)
# print(money1 <= money3)
# print(money1)
# money1.conversation("USD")
# print(money2)


class PersonError(Exception):
    pass


class CompanyError(Exception):
    pass


class JobError(Exception):
    pass


class Company:
    def __init__(self, c_m, f_a, e_c):
        if isinstance(c_m, str) and isinstance(f_a, DateandTime.Date) and isinstance(e_c, int) and e_c >= 0:
            self.__company_name = c_m
            self.__founded_at = f_a
            self.__employees_count = e_c
        else:
            raise CompanyError

    def __repr__(self):
        return "company name:{}, founded at:{},employees count:{}".format(self.__company_name, self.__founded_at,
                                                                          self.__employees_count)

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        if isinstance(value, str):
            self.__company_name = value
        else:
            raise CompanyError

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, DateandTime.Date):
            self.__founded_at = value
        else:
            raise CompanyError

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, value):
        if isinstance(value, int) and value >= 0:
            self.__employees_count = value
        else:
            raise CompanyError


class Job:
    def __init__(self, c, s, e_y, p):
        if isinstance(c, Company) and isinstance(s, Money) and isinstance(e_y, int) and e_y >= 0 and isinstance(p, str):
            self.__company = c
            self.__salary = s
            self.__experience_year = e_y
            self.__position = p
        else:
            raise JobError

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        if isinstance(value, Company):
            self.__company = value
        else:
            raise JobError

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money):
            self.__salary = value
        else:
            raise JobError

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, value):
        if isinstance(value, int) and value >= 0:
            self.__experience_year = value
        else:
            raise JobError

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, str):
            self.__position = value
        else:
            raise JobError

    def __repr__(self):
        return "company:\n{}\nsalary:{},experience year:{},position:{}".format(self.__company.__repr__(), self.__salary,
                                                                               self.__experience_year, self.__position)

    def change_salary(self, newSalary):
        self.__salary = newSalary

    def change_experience_year(self, newYear):
        self.__experience_year = newYear

    def change_position(self, newPosition):
        self.__position = newPosition


class Person:
    def __init__(self, n, s, a, g, add, fr, j):
        if isinstance(n, str):
            self.__name = n
        else:
            raise PersonError("wrong input for name")
        if isinstance(s, str):
            self.__surname = s
        else:
            raise PersonError("wrong input for surname")
        if g == "Male" or g == "Female":
            self.__gender = g
        else:
            raise PersonError("wrong input for gender")
        if a >= 0:
            self.__age = a
        else:
            raise PersonError("wrong input for age")
        if isinstance(add, str):
            self.__address = add
        else:
            raise PersonError("wrong input for address")
        if isinstance(fr, list) and all(isinstance(x, Person) for x in fr):
            self.__friends = fr
        else:
            raise PersonError("wrong input for friends")
        if isinstance(j, list) and all(isinstance(x, Job) for x in j):
            self.__job = j
        else:
            raise PersonError("wrong input for Jobs")

    def __repr__(self):
        return "name:{},surname:{},gender:{},age:{},address:{},friends:{},job:{}".format(self.__name, self.__surname,
                                                                                         self.__gender, self.__age,
                                                                                         self.__address, self.__friends,
                                                                                         self.__job)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PersonError

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            raise PersonError

    def add_friend(self, newFriend):
        self.__friends.append(newFriend)
        newFriend.__friends.append(self)

    def remove_friend(self, oldFriend):
        self.__friends.remove(oldFriend)
        oldFriend.__friends.remove(self)

    def add_job(self, newJob):
        self.__job.append(newJob)
        newJob.company.employees_count += 1

    def removeJob(self, oldJob):
        if oldJob in self.__job:
            self.__job.remove(oldJob)
            oldJob.company.employees_count -= 1

    def display_job(self):
        return self.__job


# print(c.employees_count)
c = Company("company", DateandTime.Date(2002, 6, 5), 1200)
j1 = Job(c, Money(2000, "USD"), 2020, "position1")
j2 = Job(c, Money(100, "USD"), 2010, "position2")

p1 = Person("p1", "p11", 19, "Female", "Yerevan", [], [j1])
p2 = Person("p2", "p22", 21, "Female", "Yerevan", [], [])
p3 = Person("p3", "p33", 19, "Female", "Yerevan", [], [j2])
p1.add_friend(p2)
p3.add_friend(p1)
p2.add_job(j2)


# print(p1)
# print(p2)
# print(p3)
# print(c.employees_count)
# p3.remove_job(j2)
# print(c.employees_count)


class DoctorError(Exception):
    pass


class Doctor(Person):
    def __init__(self, name, surname, age, gender, address, friends, job, department: str, profession: str,
                 patronymic: str, salary: Money):
        super().__init__(name, surname, age, gender, address, friends, job)
        if isinstance(department, str):
            self.__department = department
        else:
            raise DoctorError("Department should be a string")
        if isinstance(profession, str):
            self.__profession = profession
        else:
            raise DoctorError("Profession should be a string")
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise DoctorError("Patronymic should be a string")
        if isinstance(salary, Money):
            self.__salary = salary
        else:
            raise DoctorError("Salary should be a Money")

    def __repr__(self):
        return super(Doctor,
                     self).__repr__() + f", Department : {self.department}, Profession : {self.profession}, Patronymic : {self.patronymic}, Salary : {self.salary}"

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if isinstance(value, str):
            self.__department = value
        else:
            raise DoctorError("Department should be a string")

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value):
        if isinstance(value, str):
            self.__profession = value
        else:
            raise DoctorError("Profession should be a string")

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if isinstance(value, str):
            self.__patronymic = value
        else:
            raise DoctorError("Patronymic should be a string")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money):
            self.__salary = value
        else:
            raise DoctorError("Salary should be a Money")


p = Person("la", "lala", 12, "Male", " ", [], [])
print(p)
d = Doctor("lo", "lolo", 30, "Male", " ", [], [], "dep1", "prof", "pap", Money(100, "AMD"))
print(d)


class CityError(Exception):
    pass


class City:
    def __init__(self, name: str, major: Person, population: int, language: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise CityError("City name should be a string")
        if isinstance(major, Person):
            self.__major = major
        else:
            raise CityError("Major should be Person")
        if isinstance(population, int):
            self.__population = population
        else:
            raise CityError("Population should be integer")
        if isinstance(language, str):
            self.__language = language
        else:
            raise CityError("Language should be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise CityError("City should be a string")

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        if isinstance(value, Person):
            self.__major = value
        else:
            raise CityError("Major should be Person")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if isinstance(value, int):
            self.__population = value
        else:
            raise CityError("Population should be integer")

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if isinstance(value, str):
            self.__language = value
        else:
            raise CityError("Language should be a string")

    def __repr__(self):
        return f" Name : {self.__name}, Major : {self.__major}, Population : {self.__population}, Language : {self.__language}"


class UniversityError(Exception):
    pass


class University:
    def __init__(self, name: str, founded_at: DateandTime.Date, rector: Person, city: City):
        if isinstance(name, str):
            self.__name = name
        else:
            raise UniversityError("Name should be a string")
        if isinstance(founded_at, DateandTime.Date):
            self.__founded_at = founded_at
        else:
            raise UniversityError("This should be a Date")
        if isinstance(rector, Person):
            self.__rector = rector
        else:
            raise UniversityError("Rector should be Person")
        if isinstance(city, City):
            self.__city = city
        else:
            raise UniversityError("City should be a City")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise UniversityError("Name should be a string")

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, DateandTime.Date):
            self.__founded_at = value
        else:
            raise UniversityError("This should be a Date")

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, value):
        if isinstance(value, str):
            self.__rector = value
        else:
            raise UniversityError("Rector should be a string")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, City):
            self.__city = value
        else:
            raise UniversityError("City should be a City")

    def __repr__(self):
        return f"Name : {self.__name}, Founded in : {self.__founded_at}, Rector : {self.__rector}, City : {self.__city}"

class TeacherError(Exception):
    pass


class Teacher(Person):

    def __init__(self, name, surname, age, gender, address, friends, jobs, university: University, faculty: str,
                 experience: int,
                 start_work_at: DateandTime.Date, subject: str, salary: Money):
        super().__init__(name, surname, age, gender, address, friends, jobs)
        if isinstance(university, University):
            self.__university = university
        else:
            raise TeacherError("University should be a university")
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            raise TeacherError("Faculty should be a string")
        if isinstance(experience, int):
            self.__experience = experience
        else:
            raise TeacherError("Experience should be an integer")
        if isinstance(start_work_at, DateandTime.Date):
            self.__start_work_at = start_work_at
        else:
            raise TeacherError("This should be a Date")
        if isinstance(subject, str):
            self.__subject = subject
        else:
            raise TeacherError("Subject should be a string")
        if isinstance(salary, Money):
            self.__salary = salary
        else:
            raise TeacherError("Salary should be a Money")


@property
def university(self):
    return self.__university


@university.setter
def university(self, value):
    if isinstance(value, University):
        self.__university = value
    else:
        raise TeacherError("University should be a university")


@property
def faculty(self):
    return self.__faculty


@faculty.setter
def faculty(self, value):
    if isinstance(value, str):
        self.__faculty = value
    else:
        raise TeacherError("Faculty should be a string")


@property
def experience(self):
    return self.__experience


@experience.setter
def experience(self, value):
    if isinstance(value, int):
        self.__experience = value
    else:
        raise TeacherError("Experience should be an integer")


@property
def start_work_at(self):
    return self.__start_work_at


@start_work_at.setter
def start_work_at(self, value):
    if isinstance(value, DateandTime.Date):
        self.__start_work_at = value
    else:
        raise TeacherError("This should be a Date")


@property
def subject(self):
    return self.__subject


@subject.setter
def subject(self, value):
    if isinstance(value, str):
        self.__subject = value
    else:
        raise TeacherError("Subject should be a string")


@property
def salary(self):
    return self.__salary


@salary.setter
def salary(self, value):
    if isinstance(value, Money):
        self.__salary = value
    else:
        raise TeacherError("Salary should be a Money")


def __repr__(self):
    return super(Teacher,
                 self).__repr__() + f" University : {self.__university}, Faculty : {self.__faculty}, Experience : {self.__experience}, Start work at : {self.__start_work_at}, Subject : {self.__subject}, Salary : {self.__salary}"


class StudentError(Exception):
    pass


class Student(Person):
    def __init__(self, name, surname, age, gender, address, friends, jobs, university: University, faculty: str,
                 course: int,
                 started_at: DateandTime.Date):
        super().__init__(name, surname, age, gender, address, friends, jobs)
        if isinstance(university, University):
            self.__university = university
        else:
            raise StudentError("university should be a University")
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            raise StudentError("Faculty should be a string")
        if isinstance(course, str):
            self.__course = course
        else:
            raise StudentError("Course should be a string")
        if isinstance(started_at, DateandTime.Date):
            self.__started_at = started_at
        else:
            raise StudentError("This should be a Date")

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        if isinstance(value, University):
            self.__university = value
        else:
            raise StudentError("university should be a University")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if isinstance(value, str):
            self.__faculty = value
        else:
            raise StudentError("Faculty should be a string")

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        if isinstance(value, str):
            self.__course = value
        else:
            raise StudentError("Course should be a string")

    @property
    def started_at(self):
        return self.__started_at

    @started_at.setter
    def started_at(self, value):
        if isinstance(value, DateandTime.Date):
            self.__started_at = value
        else:
            raise StudentError("This should be a Date")

    def __repr__(self):
        return super(Student,
                     self).__repr__() + f" University : {self.__university}, Faculty : {self.__faculty}, Course : {self.__course}, Start at : {self.__started_at}"
