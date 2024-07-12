import unittest

from isla.fuzzer import GrammarFuzzer
from isla.derivation_tree import DerivationTree
from debugging_benchmark.calculator.calculator import calculator_grammar as grammar

from evogfuzz.input import Input
from evogfuzz.stochastic_universal_sampling import StochasticUniversalSampling as SUSampling


class TestStochasticUniversalSampling(unittest.TestCase):
    def test_selection(self):
        print()
        fuzzer = GrammarFuzzer(grammar)
        test_inputs = set()
        for idx in range(100):
            inp = Input(DerivationTree.from_parse_tree(fuzzer.fuzz_tree()))
            inp.fitness = idx
            test_inputs.add(inp)

        for inp in test_inputs:
            print(inp, "\t", inp.oracle, "\t", inp.fitness)

        selected = SUSampling(test_inputs, population_size=10).select_fittest_individuals()
        print("______")
        for inp in selected:
            print(inp, "\t", inp.oracle, "\t", inp.fitness)

if __name__ == "__main__":
    unittest.main()
