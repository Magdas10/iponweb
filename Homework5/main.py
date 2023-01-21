# Task 1
# Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.

def new_dict(dct, lst):
    return {key: val for key,
    val in dct.items() if key not in lst}


# print(new_dict({"name": "Johnik", "age": 25, "salary": 0, "city": "Yerevan"}, ["name", "salary"]))


# Task 2
# Get the key of a minimum value from the following dictionary.

def minimum_key(dct):
    if len(dct) == 0:
        return dct
    ls = list(dct.values())
    ls.sort()
    return [i for i in dct if dct[i] == ls[0]]


# print(minimum_key({"Physics": 82, "Math": 65, "history": 75}))


# Task 3
# Write a Python program to copy the contents of a file to another file

def copy_file(fl1, fl2):
    for line in fl1:
        fl2.write(line)


# print(copy_file(open("file1.txt", 'r'), open("file2.txt", 'w')))

# Task 4
# Write a Python program to count the frequency of words in a file

def word_count(fl):
    words = fl.read().split()
    dct = {}
    for w in words:
        if w in dct:
            dct[w] += 1
        else:
            dct[w] = 1
    return dct


# print(word_count(open("file1.txt",'r')))


# Task 5
# Write a Python program to read last n lines of a file

def last_n_lines(fl, n):
    for l in (fl.readlines()[-n:]):
        print(l, end='')


# last_n_lines(open("file1.txt",'r'),2)

# Task 6
# Write class Company
# Data members: company_name, founded_at, employees_count
# Data methods: __init__, __repr__

class Company:
    def __init__(self, c_m, f_a, e_c):
        self.company_name = c_m
        self.founded_at = f_a
        self.employees_count = e_c

    def __repr__(self):
        return "company name:{}, founded at:{},employees count:{}".format(self.company_name, self.founded_at,
                                                                          self.employees_count)


# Write class Job.
# Data members: company(Company type), salary, experience_year, position.
# Data methods: __init__, __repr__, change_salary, change_experience_year, change_postition.

class Job:
    def __init__(self, c, s, e_y, p):
        self.company = c
        self.salary = s
        self.experience_year = e_y
        self.position = p

    def __repr__(self):
        return "company:\n{}\nsalary:{},experience year:{},position:{}".format(self.company.__repr__(), self.salary,
                                                                               self.experience_year, self.position)

    def change_salary(self, newSalary):
        self.salary = newSalary

    def change_experience_year(self, newYear):
        self.experience_year = newYear

    def change_position(self, newPosition):
        self.position = newPosition


# Write class Person.
# Data members: name, surname, gender(Male or Female), age,
# address,  friends(list of Person type), job(list of Job type)
# Data methods: __init__, __repr__, add_friend, remove_friend, add_job,
# remove_job, display_job

class Person:
    def __init__(self, n, s, g, a, add, fr, j):
        self.name = n
        self.surname = s
        if g == "Male" or g == "Female":
            self.gender = g
        else:
            print("wrong input for gender")
        if a >= 0:
            self.age = a
        else:
            print("wrong input for age")
        self.address = add
        self.friends = fr
        self.job = j

    def __repr__(self):
        return "name:{},surname:{},gender:{},age:{},address:{},friends:{},job:{}".format(self.name, self.surname,
                                                                                         self.gender, self.age,
                                                                                         self.address, self.friends,
                                                                                         self.job)

    def add_friend(self, newFriend):
        self.friends.append(newFriend)
        newFriend.friends.append(self)

    def remove_friend(self, oldFriend):
        self.friends.remove(oldFriend)
        oldFriend.friends.remove(self)

    def add_job(self, newJob):
        self.job.append(newJob)
        newJob.company.employees_count += 1

    def removeJob(self, oldJob):
        if oldJob in self.job:
            self.job.remove(oldJob)
            oldJob.company.employees_count -= 1

    def display_job(self):
        return self.job


company = Company("lala1", 1919, 100)
job1 = Job(company, 150, 1, "director")
job2 = Job(company, 150, 1, "m")
job3 = Job(company, 150, 1, "m")
# print(job1)
# job1.change_salary(30)
# job1.change_experience_year(12)
# job1.change_position("another")
# print(job1)
p2 = Person("P2", "p2yan", "Female", 22, "lala2", [], [])
p3 = Person("P3", "p3yan", "Female", 22, "lala3", [p2], [])
p4 = Person("P4", "p4yan", "Female", 22, "lala4", [p2, p3], [])
p1 = Person("P1", "p1yan", "Female", 22, "lala1", [p2, p3], [job1])
# print(p1)
# p1.add_friend(p4)
# print(p1)
# print(p4)
# print(company)
p1.add_job(job2)


# print(company)
# p1.removeJob(job2)
# print(company)
# p1.removeJob(job3)
# print(company)
# print(p1.display_job())


# Task 7

# Class - Date
# Data members
# Year - integer
# Month - integer
# Day - integer
# Data methods
# Constructor - 3 params for init year, mounth, day
# __repr__ for print Date objet like - day.mount.year
# Ex. 15.10.1950
# add_day - add day to given Date object
# Add_mount - add mount to given Date object
# Add_year - add year to given Date object
# __is_leap_year - check year is leap or not
class Date:
    dct = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
           "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    __daysOfMonths = list(dct.values())

    def __init__(self, year, month, day):
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            print("wrong input")
        self.dct["February"] = 29 if self.is_leap_year() else 28
        Date.__daysOfMonths[1] = self.dct["February"]
        if isinstance(month, int) and month in range(1, 13):
            self.month = month
        else:
            print("wrong input for month")
        if isinstance(day, int) and day in range(1, self.__daysOfMonths[
                                                        month - 1] + 1):  # check if input is right, you cannot have 30 of February
            self.day = day
        else:
            print("wrong input for day")

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0

    def add_day(self, n):
        if n >= 0:
            self.day += n
            while self.day > Date.__daysOfMonths[self.month - 1]:
                self.day -= Date.__daysOfMonths[self.month - 1]
                self.add_month(1)
        else:
            print("wrong input")

    def add_month(self, n):
        if n >= 0:
            current_month = self.month
            self.month = (self.month + n) % 12
            if Date.__daysOfMonths[self.month - 1] < self.day <= 31:  # next month for March 31 will be April 30
                self.day = Date.__daysOfMonths[self.month - 1]
            self.add_year((current_month + n) // 12)
        else:
            print("wrong input")

    def add_year(self, n):
        if n >= 0:
            self.year += n
        else:
            print("wrong input")


#
date = Date(2000, 1, 31)
date.add_month(1)
print(date)
date.add_day(100)
print(date)


# Class - Time
# Data members
# Hour - int
# Minute - int
# Second - int
# Data methods
#
# __init__ constructor
# __repr__
# 3. add_second(s)
# 2. add_minute(m)
# 1.add_hour(h)
# sum() - Գումարել երկու Time տիպի օբյեկտ(հաշվի առնել, որ վայրկյանները
# գումարելուց կարող է փոխվել նաև րոպեն, րոպեները փոխվելուց նաև ժամը)
class Time:
    def __init__(self, hour, minute, second):
        if isinstance(hour, int) and hour in range(0, 25):
            self.hour = hour
        else:
            print("wrong input for hour")
        if isinstance(minute, int) and minute in range(0, 60):
            self.minute = minute
        else:
            print("wrong input for minute")
        if isinstance(second, int) and second in range(0, 60):
            self.second = second
        else:
            print("wrong input for second")

    def __repr__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def add_hour(self, n):
        if n >= 0:
            self.hour = (self.hour + n) % 24
        else:
            print("wrong input")

    def add_minute(self, n):
        if n >= 0:
            self.minute += n
            while self.minute >= 60:
                self.minute -= 60
                self.add_hour(1)
        else:
            print("wrong input")

    def add_second(self, n):
        if n >= 0:
            self.second += n
            while self.second >= 60:
                self.second -= 60
                self.add_minute(1)
        else:
            print("wrong input")

    def sum(self, other):
        result = Time(self.hour, self.minute, self.second)
        result.add_second(other.second)
        result.add_minute(other.minute)
        result.add_hour(other.hour)
        return result


time = Time(3, 58, 57)
# print(time)
# time.add_hour(26)
# print(time)
# time.add_minute(8)
# print(time)
# time.add_second(8)
# print(time)

# time1 = Time(18, 58, 58)
# print(time.sum(time1))
# print(time1.sum(time))
