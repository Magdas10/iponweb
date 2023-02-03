class RangeError(Exception):
    pass


class MyRange:
    curr = None

    def __init__(self, current, end, step):
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
        if (self.__step >= 0 and MyRange.curr >= self.end) or (self.__step < 0 and MyRange.curr < self.end):
            raise StopIteration
        else:
            MyRange.curr += self.__step
        return MyRange.curr - self.__step

    def __len__(self):
        return (self.__end - self.__current) // self.__step

    def __getitem__(self, item):
        if item > len(self):
            raise RangeError("Index out of range")
        x = MyRange.curr
        for _ in MyRange(1, item, 1):
            x += self.__step
        return x

    def __reversed__(self):
        return MyRange(self.__end - 1, self.__current, - self.__step)


r = MyRange(1, 10, 1)
# print(r)
# print(r[4])
# print(len(r))
for i in r:
    print(i)

rev = reversed(r)
print(rev)
print(len(rev))
for i in rev:
    print(i)
