from abc import ABC, abstractmethod
from dataclasses import dataclass


class Game(ABC):
    @abstractmethod
    def generate_round(self):
        pass

    @abstractmethod
    def description(self):
        pass


@dataclass
class Round:
    question: str
    answer: str
