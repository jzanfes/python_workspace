class PlayerMgmt:
    def players_new_game():
        players = []
        print('Please enter player names individually and then enter "q" when all players have been added.')
        player_entry = True
        while player_entry:
            new_player = input('Player Name:').strip()
            if new_player == 'q':
                player_entry = False
            else:
                players.append(new_player.title().strip())
                print(players)
        return tuple(players)


player_tuple = PlayerMgmt.players_new_game()
print(player_tuple)
