class TestSuite:

    def __init__(self):
        self.tests = []
    
    def run(self, result):
        print("Running Test Suite:\n")
        for test in self.tests:
            test.run(result)
    
    def add (self, test):
        self.tests.append(test)