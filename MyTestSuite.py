class MyTestSuite:

    def __init__(self):
        self.tests = []
    
    def run(self):
        print("Running Test Suite:\n")
        for test in self.tests:
            test.run()
    
    def add (self, test):
        self.tests.append(test)