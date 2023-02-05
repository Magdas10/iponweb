from copy import deepcopy


class DateError(Exception):
    pass


class Date:
    dct = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
           "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    daysOfMonths = list(dct.values())

    def __init__(self, year, month, day):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            raise DateError
        self.dct["February"] = 29 if self.is_leap_year() else 28
        Date.daysOfMonths[1] = self.dct["February"]
        if isinstance(month, int) and month in range(1, 13):
            self.__month = month
        else:
            raise DateError
        if isinstance(day, int) and day in range(1, self.daysOfMonths[month - 1] + 1):
            self.__day = day
        else:
            raise DateError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def __ge__(self, other):
        if self.__year > other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month > other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day > other.__day:
                    return True
                elif self.__day == other.__day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__year > other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month > other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day > other.__day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__year == other.__year and self.__month == other.__month and self.__day == other.__day

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
            raise DateError

    def add_month(self, n):
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                if self.__month + 1 > 12:
                    self.__month = 1
                    self.__year += 1
                else:
                    self.__month += 1
            self.dct["February"] = 29 if self.is_leap_year() else 28
            Date.daysOfMonths[1] = self.dct["February"]
            if self.month == 2 and self.day == 29:
                self.day = Date.daysOfMonths[1]
            if self.__day > Date.daysOfMonths[self.month - 1]:
                self.__day = Date.daysOfMonths[self.month - 1]
        else:
            raise DateError

    def add_day(self, n):
        if isinstance(n, int) and n >= 0:
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
            raise DateError


# print(Date(2020, 2, 13) >= Date(2020, 2, 14))


# d = Date(2000, 3, 31)
# print(d)
# d.add_month(1)
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

class TimeError(Exception):
    pass


class Time:
    def __init__(self, hour, minute, second):
        if isinstance(hour, int) and hour in range(0, 25):
            self.__hour = hour
        else:
            raise TimeError
        if isinstance(minute, int) and minute in range(0, 60):
            self.__minute = minute
        else:
            raise TimeError
        if isinstance(second, int) and second in range(0, 60):
            self.__second = second
        else:
            raise TimeError

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        self.__minute = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        self.__second = value

    def __repr__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def __ge__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minute > other.__minute:
                return True
            elif self.__minute == other.__minute:
                if self.__second > other.__second:
                    return True
                elif self.__second == other.__second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minute > other.__minute:
                return True
            elif self.__minute == other.__minute:
                if self.__second > other.__second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__hour == other.__hour and self.__minute == other.__minute and self.__second == other.__second

    def add_hour(self, n):
        if isinstance(n, int):
            self.hour = (self.hour + n) % 24
        else:
            raise TimeError

    def add_minute(self, n):
        if isinstance(n, int):
            self.minute += n
            while self.minute >= 60:
                self.minute -= 60
                self.add_hour(1)
        else:
            raise TimeError

    def add_second(self, n):
        if isinstance(n, int):
            self.second += n
            while self.second >= 60:
                self.second -= 60
                self.add_minute(1)
        else:
            raise TimeError

    def sum(self, other):
        result = Time(self.hour, self.minute, self.second)
        result.add_second(other.second)
        result.add_minute(other.minute)
        result.add_hour(other.hour)
        return result


class DateTimeError(Exception):
    pass


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
            raise DateTimeError

    def add_second(self, n):
        if isinstance(n, int):
            self.__time.second += n
            while self.__time.second >= 60:
                self.__time.second -= 60
                self.add_minute(1)
        else:
            raise DateTimeError

    def sub_year(self, n):
        self.add_year(-n)

    def sub_month(self, n):
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                if self.__date.month - 1 <= 0:
                    self.__date.year -= 1
                    self.__date.month = 12
                else:
                    self.__date.month -= 1
            self.__date.dct["February"] = 29 if self.__date.is_leap_year() else 28
            Date.daysOfMonths[1] = self.__date.dct["February"]
            if self.__date.month == 2 and self.__date.day == 29:
                self.__date.day = Date.daysOfMonths[1]
            if self.__date.day > Date.daysOfMonths[self.__date.month - 1]:
                self.__date.day = Date.daysOfMonths[self.__date.month - 1]

        else:
            raise DateTimeError

    def sub_day(self, n):
        # if isinstance(n, int) and n >= 0:
        #     for day in range(n):
        #         self.__date.dct["February"] = 29 if self.__date.is_leap_year() else 28
        #         self.__date.daysOfMonths[1] = self.__date.dct["February"]
        #         if self.__date.day == 1:
        #             self.__date.day = 31 if self.__date.month == 1 else self.__date.daysOfMonths[
        #                 self.__date.month - 2]
        #             self.__date.year = (self.__date.year - 1) if self.__date.month == 1 else self.__date.year
        #             self.__date.month = 12 if self.__date.month == 1 else (self.__date.month - 1)
        #         else:
        #             self.__date.day -= 1
        # else:
        #     raise DateTimeError
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                self.__date.dct["February"] = 29 if self.__date.is_leap_year() else 28
                Date.daysOfMonths[1] = self.__date.dct["February"]
                if self.__date.day - 1 <= 0:
                    self.__date.month = self.__date.month - 1 if self.__date.month - 1 > 0 else 12
                    self.__date.year = (self.__date.year - 1) if self.__date.month == 12 else self.__date.year
                    self.__date.day = Date.daysOfMonths[self.__date.month - 1]
                else:
                    self.__date.day -= 1

    def sub_hour(self, n):
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                if self.__time.hour - 1 < 0:
                    self.sub_day(1)
                    self.__time.hour = 23
                else:
                    self.__time.hour -= 1
        else:
            raise DateTimeError

    def sub_minute(self, n):
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                if self.__time.minute - 1 < 0:
                    self.sub_hour(1)
                    self.__time.minute = 59
                else:
                    self.__time.minute -= 1
        else:
            raise DateTimeError

    def sub_second(self, n):
        if isinstance(n, int) and n >= 0:
            for i in range(n):
                if self.__time.second - 1 < 0:
                    self.sub_minute(1)
                    self.__time.second = 59
                else:
                    self.__time.second -= 1
        else:
            raise DateTimeError

    def __ge__(self, other):
        return self.__date > other.__date or (self.date == other.__date and self.__time >= other.__time)

    # def __eq__(self, other):
    #     return self >= other >= self

    def __add__(self, other):
        result = deepcopy(self)
        result.add_second(other.time.second)
        result.add_minute(other.time.minute)
        result.add_hour(other.time.hour)
        result.add_day(other.date.day)
        result.add_month(other.date.month)
        result.add_year(other.date.year)
        return result

    def __sub__(self, other):
        if self >= other:
            result = deepcopy(self)
            result.sub_second(other.time.second)
            result.sub_minute(other.time.minute)
            result.sub_hour(other.time.hour)
            result.sub_day(other.date.day)
            result.sub_month(other.date.month)
            result.sub_year(other.date.year)
            return f"{result.__date.year} years, {result.__date.month} months, {result.__date.day} days," \
                   f"{result.__time.hour} hours, {result.__time.minute} minutes, {result.__time.second} seconds"
        else:
            raise DateTimeError

    def duration(self, other):
        result = 0
        if self >= other:
            while not self.__date == other.__date:
                other.add_day(1)
                result += 1
            if other.__time > self.__time:
                result -= 1
            return f"{result} days"
        else:
            raise DateTimeError



# dt1 = DateTime(Date(2001, 2, 28), Time(12, 34, 56))
# dt1.sub_second(8)
# print(dt1)
# dt2 = DateTime(Date(1989, 8, 20), Time(4, 7, 8))
# print(dt1 - dt2)
# print(dt1 + dt2)
# print(dt1)
# print(dt2)
# dt3 = DateTime(Date(2000, 12, 31), Time(23, 59, 59))
# print(dt2 + dt3)
# print(dt1 - dt2)
# dt = DateTime(Date(2000, 2, 29), Time(3, 58, 57))
# print(dt)
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
# # print(dt)
# dt.sub_month(12)
# print(dt)
# dt.sub_day(366)
# print(dt)
# dt.sub_hour(139)
# print(dt)
# dt.sub_hour(24)
# print(dt)
#
# dt1 = DateTime(Date(2000, 2, 29), Time(0, 0, 0))
# print(dt1)
# dt1.sub_day(366)
# print(dt1)
# dt1.sub_day(365)
# print(dt1)
# dt1.sub_hour(250)
# print(dt1)
#
# dt2 = DateTime(Date(2005, 4, 30), Time(3, 57, 12))
# print(dt2)
# dt2.sub_minute(360)
# print(dt2)
# dt2.sub_minute(5)
# print(dt2)
# dt2.sub_second(3600)
# print(dt2)
# dt2.sub_second(13)
# print(dt2)
# dt2.sub_second(19)
# print(dt2)

# d = DateTime(Date(2000, 2, 29),Time(23,59,59))
# print(d)
# d.sub_month(1)
# print(d)
# d.sub_day(366)
# print(d)
# d.sub_day(365)
# print(d)
# d.sub_day(1)
# print(d)
# d.sub_day(366)
# print(d)


# dt = DateTime(Date(2021, 3, 31), Time(23, 5, 6))
# # dt.sub_month(13)
# print(dt)
# otherr = DateTime(Date(2022, 7, 12), Time(10, 5, 1))
# print(otherr)
# print(otherr - dt)
# otherr.sub_hour(23)
# print(otherr)
# otherr.sub_minute(5)
# print(otherr)
# otherr.sub_second(6)
# print(otherr)
# print(other)

# dt1 = DateTime(Date(2020, 2, 28), Time(23, 59, 0))
# print(dt1)
# dt1.sub_month(13)
# print(dt1)

# dt11 = DateTime(Date(2020, 2, 29), Time(23, 59, 59))
# print(dt11)
# dt11.add_month(12)
# print(dt11)

# d = DateTime(Date(2020, 5, 31), Time(23, 59, 0))
# print(d)
# d.sub_month(1)
# print(d)

# print(DateTime(Date(2020, 2, 28), Time(23, 59, 0)).duration(DateTime(Date(2020, 2, 28), Time(23, 59, 0))))
# print(DateTime(Date(2021, 2, 28), Time(23, 59, 0)).duration(DateTime(Date(2020, 2, 28), Time(23, 59, 0))))
# print(DateTime(Date(2021, 2, 28), Time(22, 59, 0)).duration(DateTime(Date(2020, 2, 28), Time(23, 59, 0))))
