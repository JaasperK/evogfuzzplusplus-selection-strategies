import logging
from typing import Set, List
from evogfuzz.input import Input
import numpy as np


class Truncation:
    def __init__(self, 
                 test_inputs: Set[Input], 
                 population_size: int = 100, 
                 truncation_threshold: float = 0.5):
        
        self.test_inputs: Set[Input] = test_inputs
        self.population_size: int = population_size
        self.truncation_threshold: float = truncation_threshold

    def select_fittest_individuals(self):
        sorted_inputs = sorted(self.test_inputs, key=lambda inp: inp.fitness, reverse=True)
        trunc_index = int(len(sorted_inputs) * self.truncation_threshold)
        fittest = set(sorted_inputs[:trunc_index])
        return fittest
