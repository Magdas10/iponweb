class Date:
    dct = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
           "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    daysOfMonths = list(dct.values())

    def __init__(self, year, month, day):
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            print("wrong input")
        self.dct["February"] = 29 if self.is_leap_year() else 28
        Date.daysOfMonths[1] = self.dct["February"]
        if isinstance(month, int) and month in range(1, 13):
            self.month = month
        else:
            print("wrong input for month")
        if isinstance(day, int) and day in range(1, self.daysOfMonths[
                                                        month - 1] + 1):  # check if input is right, you cannot have 30 of February
            self.day = day
        else:
            print("wrong input for day")

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0

    def add_year(self, n):
        if isinstance(n, int):
            self.year += n
            self.dct["February"] = 29 if self.is_leap_year() else 28
            Date.daysOfMonths[1] = self.dct["February"]
            if self.month == 2 and self.day == 29:
                self.day = Date.daysOfMonths[1]
        else:
            print("wrong input")

    def add_month(self, n):
        if isinstance(n, int):
            self.month = (self.month + n) % 12 if (self.month + n) % 12 != 0 else 12
            self.year += (self.month + n) // 12
            self.dct["February"] = 29 if self.is_leap_year() else 28
            Date.daysOfMonths[1] = self.dct["February"]
            if Date.daysOfMonths[self.month - 1] < self.day:
                self.day = Date.daysOfMonths[self.month - 1]
        else:
            print("wrong input")

    def add_day(self, n):
        if isinstance(n, int):
            for day in range(n):
                self.dct["February"] = 29 if self.is_leap_year() else 28
                Date.daysOfMonths[1] = self.dct["February"]
                if self.day == Date.daysOfMonths[self.month - 1]:
                    self.day = 1
                    self.year = (self.year + 1) if self.month == 12 else self.year
                    self.month = 1 if self.month == 12 else (self.month + 1)
                else:
                    self.day += 1
        else:
            print("wrong input")


# d = Date(2000, 2, 29)
# print(d)
# d.add_month(1)
# print(d)
# d.add_day(366)
# print(d)
# d.add_day(365)
# print(d)
# d.add_day(1)
# print(d)
# d.add_day(366)
# print(d)

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
        if isinstance(n, int):
            self.hour = (self.hour + n) % 24
        else:
            print("wrong input")

    def add_minute(self, n):
        if isinstance(n, int):
            self.minute += n
            while self.minute >= 60:
                self.minute -= 60
                self.add_hour(1)
        else:
            print("wrong input")

    def add_second(self, n):
        if isinstance(n, int):
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


class DateTime:
    def __init__(self, date, time):
        self.__date = date
        self.__time = time

    def __repr__(self):
        return f"date: {Date.__repr__(self.__date)}, time: {Time.__repr__(self.__time)}"

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    # @date.getter
    # def date(self):
    #     return self.__date

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    # @time.getter
    # def time(self):
    #     return self.__time

    def add_year(self, n):
        self.__date.add_year(n)

    def add_month(self, n):
        self.__date.add_month(n)

    def add_day(self, n):
        self.__date.add_day(n)

    def add_hour(self, n):
        self.add_day((self.__time.hour + n) // 24)
        self.__time.add_hour(n)

    def add_minute(self, n):
        if isinstance(n, int):
            self.__time.minute += n
            while self.__time.minute >= 60:
                self.__time.minute -= 60
                self.add_hour(1)
        else:
            print("wrong input")

    def add_second(self, n):
        if isinstance(n, int):
            self.__time.second += n
            while self.__time.second >= 60:
                self.__time.second -= 60
                self.add_minute(1)
        else:
            print("wrong input")

    def sub_year(self, n):
        self.add_year(-n)

    def sub_month(self, n):
        self.add_month(-n)

    def sub_day(self, n):
        if isinstance(n, int) and n >= 0:
            for day in range(n):
                self.__date.dct["February"] = 29 if self.__date.is_leap_year() else 28
                self.__date.daysOfMonths[1] = self.__date.dct["February"]
                if self.__date.day == 1:
                    self.__date.day = 31 if self.__date.month == 1 else self.__date.daysOfMonths[
                        self.__date.month - 2]
                    self.__date.year = (self.__date.year - 1) if self.__date.month == 1 else self.__date.year
                    self.__date.month = 12 if self.__date.month == 1 else (self.__date.month - 1)
                else:
                    self.__date.day -= 1
        else:
            print("wrong input")

    def sub_hour(self, n):
        self.sub_day((self.__time.hour + n) // 24)
        self.__time.add_hour(-n)


dt = DateTime(Date(2000, 2, 29), Time(3, 58, 57))
print(dt)
# dt.add_month(1)
# print(dt)
# dt.add_day(366)
# print(dt)
# print(dt.date)
# dt.date = Date(2001, 1, 31)
# print(dt)
# dt.add_month(13)
# print(dt)
# dt.add_hour(139)
# print(dt)
# dt.add_second(123000)
# print(dt)
dt.sub_month(12)
print(dt)
dt.sub_day(366)
print(dt)
dt.sub_hour(139)
print(dt)
