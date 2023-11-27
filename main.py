from game import TicTacToe, play
from player import RandomComputerPlayer, SmartComputerPlayer


def call(player):
    player_ch = int(input(f"\n1. Random\n2. AI\nWho is player '{player}': "))
    if player_ch == 1:
        return RandomComputerPlayer(player)
    else:
        return SmartComputerPlayer(player)


num = int(input("Number of games: "))
x_player = call('X')
o_player = call('O')

wins = [0, 0, 0]

for i in range(num):
    print("Running game no:", i)
    win = play(TicTacToe(), x_player, o_player)
    if wins == 'X':
        wins[0] += 1
    elif wins == 'O':
        wins[2] += 1
    else:
        wins[1] += 1

print('\n\nX wins:', wins[0], '\nO wins:', wins[2], '\nDraw:', wins[1])
