def ForAttr(cls):
    def decorator(func):
        def result(self = None, *a, **kw):
            for __attr__ in [
                __attr__ for __attr__ in dir(cls)
                if not __attr__.startswith('__')
                and not callable(getattr(cls, __attr__))
            ]:
                func(self, __attr__, *a, **kw)

        return result
    return decorator
