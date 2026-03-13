class BenchmarkCase:
    def __init__(self, question, expected):
        self.question = question
        self.expected = expected


class Benchmark:
    def __init__(self):
        self.cases = []

    def add_case(self, question, expected):
        self.cases.append(BenchmarkCase(question, expected))
