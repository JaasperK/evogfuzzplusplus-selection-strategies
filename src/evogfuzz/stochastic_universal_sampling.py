import logging
from typing import Set, List
from evogfuzz.input import Input
import numpy as np
import random

class StochasticUniversalSampling:
    def __init__(self, test_inputs: Set[Input], population_size: int = 100):
        """
        Initialize the Stochastic Universal Sampling selection strategy.

        Args:
        - test_inputs (Set[Input]): Set of Input objects to select from.
        - population_size (int): Number of individuals to select.
        """
        self.test_inputs = test_inputs
        self.population_size = population_size

    def select_fittest_individuals(self) -> Set[Input]:
        """
        Select the fittest individuals using the Stochastic Universal Sampling strategy.

        Returns:
        - Set[Input]: Set of selected Input objects.
        """
        # Calculate total fitness of all inputs
        total_fitness = sum(inp.fitness for inp in self.test_inputs)
        
        # If total fitness is zero, return an empty set
        if total_fitness == 0:
            return set()

        # Calculate distance between pointers
        pointers_distance = total_fitness / self.population_size
        
        # Start with a random point within the first segment
        start_point = random.uniform(0, pointers_distance)

        selected_individuals = set()
        fitness_sum = 0.0
        current_input = iter(self.test_inputs)

        # Iterate over the population size to select individuals
        for i in range(self.population_size):
            pointer = start_point + i * pointers_distance
            while fitness_sum < pointer:
                try:
                    current_individual = next(current_input)
                    fitness_sum += current_individual.fitness
                except StopIteration:
                    break
            selected_individuals.add(current_individual)

        return selected_individuals