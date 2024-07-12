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
<<<<<<< HEAD
    TOURNAMENT = 0
    TRUNCATION = 1
    ROULETTE = 2
    RANK = 3
    STOCHASTIC_UNIVERSAL_SAMPLING = 4
=======
    TOURNAMENT = "Tournament"
    TRUNCATION = "Truncation"
    ROULETTE = "Roulette"
    RANK = "Rank"
>>>>>>> 5157a0964daf4a86616a5ee797fae697745a39c1

    def __str__(self) -> str:
        return self.value