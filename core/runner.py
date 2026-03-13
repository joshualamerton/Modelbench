from core.metrics import exact_match


class Runner:
    def __init__(self):
        self.strategies = {}

    def add_strategy(self, name, func):
        self.strategies[name] = func

    def run(self, benchmark):
        results = {}

        for strategy_name, strategy_func in self.strategies.items():
            total = 0
            details = []

            for case in benchmark.cases:
                output = strategy_func(case.question)
                score = exact_match(case.expected, output)
                total += score
                details.append({
                    "question": case.question,
                    "expected": case.expected,
                    "output": output,
                    "score": score
                })

            accuracy = total / len(benchmark.cases) if benchmark.cases else 0
            results[strategy_name] = {
                "accuracy": accuracy,
                "details": details
            }

        return results
