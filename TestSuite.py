class TestSuite:

    def __init__(self):
        self.tests = []
    
    def run(self, result):
        for test in self.tests:
            test.run(result)
    
    def add_test (self, test):
        self.tests.append(test)