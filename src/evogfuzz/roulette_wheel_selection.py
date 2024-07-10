from typing import Set
from evogfuzz.input import Input
import numpy as np


class Roulette:
    """
    Implements the roulette wheel selection strategy for selecting fittest individuals from a given set of inputs.

    Attributes:
        test_inputs (Set[Input]): A set of input individuals to select from.
        tournament_rounds (int): Number of rounds for the selection process.
        tournament_size (int): Size of each selection round.
        total_fitness (float): Total fitness of all input individuals combined, used to determine selection probabilities.
    """

    def __init__(
        self,
        test_inputs: Set[Input],
        tournament_rounds: int = 10,
        tournament_size: int = 10,
    ) -> None:
        """
        Initialize the Roulette selection strategy.

        :param test_inputs: A set of input individuals to select from.
        :param tournament_rounds: Number of rounds for the selection process.
        :param tournament_size: Size of each selection round.
        """
        self.test_inputs: Set[Input] = test_inputs
        self.tournament_rounds: int = tournament_rounds
        self.tournament_size: int = tournament_size
        self.total_fitness: float = sum(input.fitness for input in test_inputs)

    def select_fittest_individuals(self) -> Set[Input]:
        """
        Select the fittest individuals based on the roulette wheel selection strategy.

        :return: A set of the fittest selected individuals.
        """
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
