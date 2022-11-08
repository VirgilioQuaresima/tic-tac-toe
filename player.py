from abc import ABC, abstractmethod

class Player:

    def __init__(self, name: str, symbol: str) -> None:
        self.symbol = symbol
        self.name = name

    def add_pad(self) -> tuple:
        pos = input(f'{self.name} select a pad: ')
        row, col = tuple(pos.split('-'))
        return int(row), int(col)
