from TestCase import TestCase
from TestSuite import TestSuite
from TestResult import TestResult

class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')

result = TestResult()

test1 = MyTest('test_a')
test1.run(result)

test2 = MyTest('test_b')
test2.run(result)

test3 = MyTest('test_c')
test3.run(result)

print(result.summary())

suiteResult = TestResult()

suite = TestSuite()
suite.add_test(test1)
suite.add_test(test2)
suite.add_test(test3)

suite.run(suiteResult)

print(suiteResult.summary())