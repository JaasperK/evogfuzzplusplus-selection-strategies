from random import choices
from typing import Set, List
from evogfuzz.input import Input

class Rank:
    """
    Class for performing rank-based selection on a set of Inputs.

    Attributes:
        test_inputs (Set[Input]): The set of Inputs to pick from.
        selective_pressure (float): 1.0 <= sp <= 2.0, Selective pressure parameter influencing the selection probability distribution. 
        m (int): The number of Inputs to be selected.
    """
     
    def __init__(
        self,
        test_inputs: Set[Input],
        selective_pressure: float,
        m: int,
    ) -> None:
        self.test_inputs : Set[Input] = test_inputs
        self.sp: float = selective_pressure
        self.m: int = m

    
    def select_fittest_individuals(self) -> List[Input]:
        sorted_inputs: List[Input] = sorted(self.test_inputs, key=lambda i: i.fitness, reverse=True)
        ranks: List[int] = list(range(1, len(sorted_inputs) + 1))

        selection_probabilities = Rank.linear_ranking_selection_probs(ranks, self.sp)

        fittest: List[Input] = choices(sorted_inputs, weights=selection_probabilities, k=self.m)        
        return set(fittest)
    
    
    def simple_selection_probs(ranks: List[int]) -> List[float]:
        ranks_sum = sum(ranks)
        return [r / ranks_sum for r in reversed(ranks)]


    # See: A. Sokolov et al. "A note on the variance of rank-based selection strategies for genetic algorithms and genetic programming"
    def linear_ranking_selection_probs(ranks: List[int], S: float):
        P = float(len(ranks))
        probs = [(S - (2.0 - S)) * (P - i) / (P - 1) + (2.0 - S) for i in ranks]
        return [prob / P for prob in probs]

