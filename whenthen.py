def whenthen(func):
    when_then_all = []
    when_then = []

    def wrapper(*args, **kwargs):
        for cond in when_then_all:
            if cond[0](*args, **kwargs):
                return cond[1](*args, **kwargs)
        return func(*args, **kwargs)

    def when(whenfunc):
        if not when_then:
            when_then.append(whenfunc)
        else:
            raise ValueError
        return wrapper

    def then(thenfunc):
        if when_then:
            when_then.append(thenfunc)
            when_then_all.append(when_then.copy())
            when_then.clear()
        else:
            raise ValueError
        return wrapper

    wrapper.when = when
    wrapper.then = then
    return wrapper