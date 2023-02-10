from enum import Enum
from colorama import Fore

__all__ = ["TicTacToe","Player","NoMoreMovesError", "MovesNotAllowedError", "MoveOutofBoundError"]

class Player(Enum):
    FIRST:int = 0
    SECOND :int = 1


class TicTacToe:
    board = """
    + - - - + - - - + - - - +
    |       |       |       | 
    |   {}   |   {}   |   {}   | 
    |       |       |       | 
    + - - - + - - - + - - - + 
    |       |       |       | 
    |   {}   |   {}   |   {}   | 
    |       |       |       | 
    + - - - + - - - + - - - + 
    |       |       |       | 
    |   {}   |   {}   |   {}   | 
    |       |       |       | 
    + - - - + - - - + - - - +"""

    def __init__(self) -> None:
        self.moves = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.count = 0

    @staticmethod
    def position2d(pos):
        pos = pos -1
        return (pos//3, pos%3)

    def move(self, player: Player, pos: int):
        if self.count >= 9:
            raise NoMoreMovesError()

        if pos > 9 or pos < 1:
            raise MoveOutofBoundError()

        x, y  = self.position2d(pos)
        if isinstance(self.moves[x][y],str):
            raise MovesNotAllowedError()

        self.count += 1
        if player == Player.FIRST:
            self.moves[x][y] = "X"
        else:
            self.moves[x][y] = "O"


    def possibleMoves(self):
        for move in self.moves:
            yield move

        for i in range(3):
            move = [self.moves[j][i] for j in range(3)]
            yield move
        
        move = [self.moves[i][i] for i in range(3)]
        yield move
        move = [self.moves[i][2-i] for i in range(3)]
        yield move


    def checkWinner(self) -> Player:
        for move in self.possibleMoves():
            if set(move) == set(["X"]):
                return Player.FIRST

            elif set(move) == set(["O"]):
                return Player.SECOND

    def render(self) -> str:
        tmoves = []
        for i in range(3):
            for j in range(3):
                if self.moves[i][j] == "X":
                    tmoves.append(f"{Fore.RED}X{Fore.WHITE}")
                elif self.moves[i][j] == "O":
                    tmoves.append(f"{Fore.GREEN}O{Fore.WHITE}")
                else:
                    tmoves.append(f"{Fore.BLACK}{self.moves[i][j]}{Fore.WHITE}")
        return self.board.format(*tmoves)


class NoMoreMovesError(Exception):
    pass

class MovesNotAllowedError(Exception):
    pass

class MoveOutofBoundError(Exception):
    pass