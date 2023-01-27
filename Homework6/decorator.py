dt = {}


def decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if fn.__name__ in dt:
            dt[fn.__name__] += 1
        else:
            dt[fn.__name__] = 1
        return result

    return wrapper


@decorator
def lala():
    return 100


lala()
lala()
print(dt)
