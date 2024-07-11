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
        
        self.test_inputs: Set[Input] = test_inputs
        self.population_size: int = population_size
        self.truncation_threshold: float = truncation_threshold

    def select_fittest_individuals(self) -> Set[Input]:
        sorted_inputs = sorted(self.test_inputs, key=lambda inp: inp.fitness, reverse=True)
        trunc_index = int(len(sorted_inputs) * self.truncation_threshold)
        selected_individuals = sorted_inputs[:trunc_index]
        
        fittest = set()
        for _ in range(self.population_size):
            r = random.randint(int((1 - self.truncation_threshold) * len(sorted_inputs)), 
                               len(sorted_inputs) - 1)
            fittest.add(selected_individuals[r])
        
        return fittest