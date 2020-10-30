import unittest
from tests.register_test import RegistrationTest

# load test case
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

# create test suite 
test_suite = unittest.TestSuite([registration_test])

# run test 
unittest.TextTestRunner(verbosity=2).run(test_suite)