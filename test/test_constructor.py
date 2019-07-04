from unittest import TestCase
from src.constructor import *
from src.treat_error import *

class AllArgsConstructorTestCase(TestCase):

    def test_defaultUnrequired(self):

        @AllArgsConstructor()
        class Cls:
            pass

        try:
            cls = Cls()
        except:
            self.fail('Unexpected error has been raisen by class creation')

    @expectError(ValueError)
    def test_requiredArg(self):

        @AllArgsConstructor(required = True)
        class Cls:
            attr = None

        cls = Cls()
