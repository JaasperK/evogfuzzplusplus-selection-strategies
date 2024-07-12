import logging
from typing import Set, List
from evogfuzz.input import Input
import numpy as np
import random

class StochasticUniversalSampling:
    def __init__(self, 
                 test_inputs: Set[Input], 
                 population_size: int = 100):
        # set of input individuals 
        self.test_inputs: Set[Input] = test_inputs
        self.population_size: int = population_size

    def select_fittest_individuals(self) -> Set[Input]:
        # calculate total fitness
        total_fitness = sum(inp.fitness for inp in self.test_inputs)
        pointers_distance = total_fitness / self.population_size
        start_point = random.uniform(0, pointers_distance)

        selected_individuals = set()
        pointers = [start_point + i * pointers_distance for i in range(self.population_size)]
        fitness_sum = 0.0
        current_input = iter(self.test_inputs)
        # get the first individual
        current_individual = next(current_input)

        for pointer in pointers:
            # move along the population until the fitness_sum exceeds the pointer value
            while fitness_sum < pointer:
                fitness_sum += current_individual.fitness
                try:
                    # move to the next individual
                    current_individual = next(current_input)
                except StopIteration:
                    # stop if we reach the end of the list
                    break
            selected_individuals.add(current_individual)
        
        return selected_individuals