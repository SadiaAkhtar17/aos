import unittest
import aos_methods as methods
import aos_locators as locators


class AOSPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():
        methods.setUp()
        methods.create_new_user()
        methods.validated_new_user_created()
        methods.log_out()
        methods.log_in()
        methods.validated_user_login()
        methods.log_out()
        methods.tearDown()



