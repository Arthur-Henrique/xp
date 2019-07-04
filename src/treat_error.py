# Define an decorator to wrap a test code that need to verify for an error
def expectError(expected_errors, resolve = None):
    def decorator(test):
        def do(self):
            try:
                test(self)
            except expected_errors:
                'the expected exceptioon was raised'
            except:
                raise
            else:
                self.fail('Some of the followings errors were expected: {expected_errors}')
            finally:
                if resolve is not None:
                    resolve()

        return do
    return decorator


class NonExpectError:
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):

        def decoreted(__self__, *a, **kw):
            try:
                func(__self__, *a, **kw)
            except:
                pass
            else:
                pass
            finally:
                pass

        return decoreted
