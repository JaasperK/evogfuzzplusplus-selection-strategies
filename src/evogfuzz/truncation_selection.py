import logging
from typing import Set, List
from evogfuzz.input import Input
import numpy as np
import random

class Truncation:
    def __init__(self, 
                 test_inputs: Set[Input], 
                 population_size: int = 100, 
                 truncation_threshold: float = 0.5):
        """
        Initialize the Truncation selection strategy.

        Args:
        - test_inputs (Set[Input]): Set of Input objects to select from.
        - population_size (int): Number of individuals to select.
        - truncation_threshold (float): Percentage of top individuals to consider for selection.
        """
        self.test_inputs: Set[Input] = test_inputs
        self.population_size: int = population_size
        self.truncation_threshold: float = truncation_threshold

    def select_fittest_individuals(self) -> Set[Input]:
        """
        Select the fittest individuals using the Truncation selection strategy.

        Returns:
        - Set[Input]: Set of selected Input objects.
        """
        # Sort inputs by fitness in descending order
        sorted_inputs = sorted(self.test_inputs, key=lambda inp: inp.fitness, reverse=True)
        
        # Calculate truncation index based on the truncation threshold
        trunc_index = int(len(sorted_inputs) * self.truncation_threshold)
        trunc_index = max(1, min(trunc_index, len(sorted_inputs)))

        # Select fittest individuals up to truncatin index
        selected_individuals = sorted_inputs[:trunc_index]

        # If no individuals are selected due to empty sorted_inputs list, return an empty set
        if not selected_individuals:
            print("No individuals selected due to empty selected_individuals list.")
        
        # Randomly select individuals from the selected top individuals to meet the population size
        fittest = set()
        for _ in range(self.population_size):
            r = random.randint(0, len(selected_individuals) - 1)
            fittest.add(selected_individuals[r])
        
        return fittest