import random


def players_new_game():
    players = []
    print('Please enter player names individually and then enter "q" when all players have been added.')
    player_entry = True
    while player_entry:
        new_player = input('Player Name:').lower().strip()
        if new_player == 'q':
            break
        else:
            players.append(new_player.title().strip())
            print(players)
    return tuple(players)

def lead_player(players):
    player = random.choice(players)
    print(f'The first player will be {player}!')
    return(player)

def player_rotation(players, last_player):
    if players[-1] == last_player:
        next_player = players[0]
    else:
        x = players.index(last_player)
        next_player = players[x + 1]
    return next_player




# players = players_new_game()
# print(players)
# first_up = lead_player(players)
# next_up = player_rotation(players,first_up)
# print(next_up)

