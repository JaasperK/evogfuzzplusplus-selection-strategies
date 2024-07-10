from typing import Set
from evogfuzz.input import Input
import numpy as np


class Roulette:
    def __init__(
        self,
        test_inputs: Set[Input],
        tournament_rounds: int = 10,
        tournament_size: int = 10,
    ) -> None:
        self.test_inputs: Set[Input] = test_inputs
        self.tournament_rounds: int = tournament_rounds
        self.tournament_size: int = tournament_size
        self.total_fitness: float = sum(input.fitness for input in test_inputs)

    def select_fittest_individuals(self) -> Set[Input]:
        fittest: list[Input] = []
        for _ in range(self.tournament_rounds):
            for _ in range(min(self.tournament_size, len(self.test_inputs) - len(fittest))):
                pick = np.random.uniform(0, self.total_fitness)
                current = 0
                for input in self.test_inputs:
                    current += input.fitness
                    if current > pick:
                        fittest.append(input)
                        break
            if len(fittest) >= len(self.test_inputs):
                break
        return set(fittest)
