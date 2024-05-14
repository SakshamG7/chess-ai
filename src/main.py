"""
The program to create and train an AI to play the game of chess with genetic algorithms.
@author: Saksham Goel
@version: 0.1
@date: May 14, 2024
"""

from typing import List, Tuple
import random

# Creates a base AI with the set weights and decision base according to the parameters size
def create_ai(weightParam, decisionParam) -> Tuple[int, int, int]:
    weights = list(range(weightParam)) # each weight corresponds to the AI's decision per board, with set parameters
    decision_base = list(range(weightParam)) # each decision corresponds to the AI's decision per board, with set parameters
    return weights, decision_base

def call_move(color: int, x: int, y: int, piece: int, board: List[List[str]]) -> None:

    return

# Better score is determined with the ratio of peices lost, wins, draws, losses, and the number of moves
def measure_performance(board: List[List[str]], turn: int, last_move: Tuple[int, int, int]) -> int:
    return 0

def token_to_move(token: int) -> Tuple[int, int, int, int, int, int]:
    # first number represents which side moves, next 2 numbers represents the piece type, the next 2 represents the final x position, the 2 represents the final y position, the next 2 represent the initial x position, and the final 2 numbers represents the initial y position.
    # 0 = white, 1 = black
    color = token % 100000000000
    pieceIndex = []
    pass
