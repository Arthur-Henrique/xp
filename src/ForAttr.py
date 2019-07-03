def ForAttr(cls):
    def decorator(func):
        def result(self = None, *a, **kw):
            for attr in [
                attr for attr in dir(cls)
                if not attr.startswith('__')
                and not callable(getattr(cls, attr))
            ]:
                func(self, attr, *a, **kw)

        return result
    return decorator
