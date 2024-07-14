from enum import Enum


class Scenario(Enum):
    FUZZING = "Fuzzing"
    GENERATOR = "Generator"

    def __str__(self):
        return self.value


class GrammarType(Enum):
    MUTATED = "mutated"
    LEARNED = "learned"

    def __str__(self):
        return self.value


class Strategy(Enum):
    TOURNAMENT = "Tournament"
    TRUNCATION = "Truncation"
    ROULETTE = "Roulette"
    RANK = "Rank"
    STOCHASTIC_UNIVERSAL_SAMPLING = "Stochastic Universal Sampling"

    def __str__(self) -> str:
        return self.value