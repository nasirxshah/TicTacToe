from . import *
import os

def playGame():
    game = TicTacToe()
    
    player = Player.FIRST

    while True:
        try:
            pos = int(input(f">>>{player}:: "))
            if os.name == "nt":
                os.system('cls')
            else:
                os.system('clear')
                
            game.move(player=player,pos=pos)
            print(game.render())
            winner = game.checkWinner()
            if winner:
                print(f"winner:: {winner}")
                break
        
            player =  Player.FIRST if player == Player.SECOND else Player.SECOND
        except NoMoreMovesError:
            print("No Winner: Game Draw")
            break
        except (MoveOutofBoundError, MovesNotAllowedError):
            print("wrong move: try again...")

