from MyTestCase import MyTestCase
from MyTestSuite import MyTestSuite

class MyTest(MyTestCase):

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

test1 = MyTest('test_a')
test1.run()

test2 = MyTest('test_b')
test2.run()

test3 = MyTest('test_c')
test3.run()

suite = MyTestSuite()
suite.add(test1)
suite.add(test2)
suite.add(test3)

suite.run()