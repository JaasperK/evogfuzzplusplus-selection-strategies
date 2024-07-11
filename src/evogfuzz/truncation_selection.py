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
        #print(f"Total inputs: {len(sorted_inputs)}")
        
        # Calculate truncation index
        trunc_index = int(len(sorted_inputs) * self.truncation_threshold)
        trunc_index = max(1, min(trunc_index, len(sorted_inputs)))
        #print(f"Truncation index: {trunc_index}")

        # Select fittest individuals
        selected_individuals = sorted_inputs[:trunc_index]
        #print(f"Selected individuals: {len(selected_individuals)}")

        fittest = set()
        if selected_individuals:
            for _ in range(self.population_size):
                r = random.randint(0, len(selected_individuals) - 1)
                #print(f"Random index r: {r}")
                fittest.add(selected_individuals[r])
        else:
            print("No individuals selected due to empty selected_individuals list.")
        
        return fittest