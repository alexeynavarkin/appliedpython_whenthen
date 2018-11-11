def whenthen(func):
    when_then_all = []
    when_then = []

    def when(whenfunc):
        if not when_then:
            when_then.append(whenfunc)
        else:
            raise ValueError

    def then(thenfunc):
        if when_then:
            when_then.append(thenfunc)
            when_then_all.append(when_then.copy())
            when_then.clear()
        else:
            raise ValueError

    def wrapper(*args, **kwargs):
        for cond in when_then_all:
            if cond[0](*args, **kwargs):
                return cond[1](*args, **kwargs)
        return func(*args, **kwargs)

    wrapper.when = when
    wrapper.then = then
    return wrapper


def whenthen_v2(func):
    func.when_then_all = []
    func.when_then = []

    def when(whenfunc):
        if not func.when_then:
            func.when_then.append(whenfunc)
        else:
            raise ValueError

    def then(thenfunc):
        if func.when_then:
            func.when_then.append(thenfunc)
            func.when_then_all.append(func.when_then.copy())
            func.when_then.clear()
        else:
            raise ValueError

    def wrapper(*args, **kwargs):
        for cond in func.when_then_all:
            if cond[0](*args, **kwargs):
                return cond[1](*args, **kwargs)
        return func(*args, **kwargs)

    wrapper.when = when
    wrapper.then = then
    return wrapper
