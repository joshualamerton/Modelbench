from core.runner import Runner
from core.benchmark import Benchmark


def strategy_a(question):
    mapping = {
        "What is the capital of France?": "Paris",
        "What is the capital of Spain?": "Madrid",
        "What is the capital of Germany?": "Berlin"
    }
    return mapping.get(question, "Unknown")


def strategy_b(question):
    mapping = {
        "What is the capital of France?": "Paris, France",
        "What is the capital of Spain?": "Madrid",
        "What is the capital of Germany?": "Munich"
    }
    return mapping.get(question, "Unknown")


def main():
    benchmark = Benchmark()

    benchmark.add_case("What is the capital of France?", "Paris")
    benchmark.add_case("What is the capital of Spain?", "Madrid")
    benchmark.add_case("What is the capital of Germany?", "Berlin")

    runner = Runner()
    runner.add_strategy("strategy_a", strategy_a)
    runner.add_strategy("strategy_b", strategy_b)

    results = runner.run(benchmark)

    for strategy, result in results.items():
        print(f"\n{strategy} accuracy: {result['accuracy']:.2f}")
        for row in result["details"]:
            print(row)


if __name__ == "__main__":
    main()
