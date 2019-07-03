from unittest import TestCase

class AllArgsConstructorTestCase(TestCase):

    def test_defaultUnrequired(self):

        @AllArgsConstructor
        class A:
            pass

        try:
            a = A()
        except:
            self.fail('Unexpected error raisen by class creation')

    def test_:
        pass
