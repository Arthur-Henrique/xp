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

def AllArgsConstructor(required = False):
    def decorator(cls):

        def __init__(self, *a, **kw):

            nonPresentArgs = []
            @ForAttr(cls = cls)
            def loop(self, attr, *a, **kw):
                try:
                    setattr(self, attr, kw[attr])
                except KeyError:
                    nonPresentArgs.append(attr)

            loop(self, *a, **kw)

            if required and nonPresentArgs:
                raise ValueError(str(nonPresentArgs) + ' are required')

        setattr(cls, "__init__", __init__)

        return cls
    return decorator


@AllArgsConstructor()
class C:
    euq = 'default'
    p = ''
    f=None
    pass

# c = C()
# print(c.euq)
c = C(euq="EUQ2", p="q", h=1, f='1')

@ForAttr(cls = C)
def printe(self, attr): print(getattr(c, attr))

printe()
