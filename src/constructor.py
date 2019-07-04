from .for_attr import *

class AllArgsConstructor:
    required = None

    def __init__(self, required = False):
        self.required = required

    def __call__(self, cls):

        def constructor(obj, *a, **kw):

            nonPresentArgs = []
            @ForAttr(cls = cls)
            def setAttributes(obj, __attr__, *a, **kw):
                try:
                    setattr(obj, __attr__, kw[__attr__])
                except KeyError:
                    nonPresentArgs.append(__attr__)

            setAttributes(obj, *a, **kw)

            if self.required and nonPresentArgs:
                raise ValueError(str(nonPresentArgs) + ' are required')

        setattr(cls, "__init__", constructor)
        return cls



def AAllArgsConstructor(required = False):
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
