from .ForAttr import *

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
