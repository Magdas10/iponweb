class RangeError(Exception):
    pass


class MyRange:
    curr = None

    def __init__(self, current, end, step):
        if current < end and step < 0 or current > end and step > 0 or current == end and step != 0:
            raise RangeError
        if isinstance(current, int) and isinstance(end, int) and isinstance(step, int):
            self.__current = current
            self.__end = end
            self.__step = step
            MyRange.curr = current
        else:
            raise RangeError

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, value):
        if isinstance(value, int):
            self.__current = value
        else:
            raise RangeError

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, value):
        if isinstance(value, int):
            self.__end = value
        else:
            raise RangeError

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, value):
        if isinstance(value, int):
            self.__step = value
        else:
            raise RangeError

    def __repr__(self):
        return f"[{self.__current}:{self.__end}:{self.__step}]"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__step == 0:
            print(self.__current)
            raise StopIteration
        elif self.__step > 0 and self.__current > self.__end:
            raise StopIteration
        elif self.__step < 0 and self.__current < self.__end:
            raise StopIteration
        self.__current += self.__step
        return self.__current - self.__step

    def __len__(self):
        return ((self.__end - self.__current) // self.__step) + 1

    def __getitem__(self, item):
        if type(item) != int or item < 0 or item >= len(self):
            raise RangeError("Index out of range.")
        curr = self.__current
        curr_ind = 0
        for num in self:
            if curr_ind == item:
                self.__current = curr
                return num
            curr_ind += 1

    def __reversed__(self):
        return MyRange(self.__end - 1, self.__current, - self.__step)


r = MyRange(1, 10, 2)
print(r)
print(r[4])
print(len(r))
# for i in r:
#     print(i)

rev = reversed(r)
# print(rev)
# print(len(rev))
# for i in rev:
#     print(i)
