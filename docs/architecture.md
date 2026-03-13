# ModelBench Architecture

ModelBench evaluates multiple strategies over the same benchmark cases.

## Core components

### Benchmark
Stores question, expected answer, and optional metadata.

### Runner
Executes strategies on each benchmark case.

### Metrics
Calculates scores for each strategy.

## Execution flow

1. Load benchmark cases.
2. Register strategies.
3. Run each strategy against each case.
4. Score outputs.
5. Print or export results.

## Goal

The goal is to make prompt and agent evaluation repeatable and comparable.
