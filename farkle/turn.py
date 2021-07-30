import dice
import score as sc
import input

scores_list = []
turn = True
z = 0
while turn:
    if z == 0:
        print('First Roll Here We GO!')
    else:
        print('Keep trucking! Rolled 6 new dice!')
    roll = dice.init_roll()
    print(roll)
    score = sc.turn_score(roll)
    print(f'Roll score {score}!')
    if score == 0:
        print(f'{roll} Farkle!!')
        scores_list = []
        break
    elif sc.all_dice_score_chk(roll):
        scores_list.append(score)
        x = input.input_chk("All dice scored, would you like to roll again? y/n", 'y', 'n')
        if x == 'y':
            z = 1
            continue
        else:
            turn = False
            break
    else:
        if z == 0:
            x = input.input_chk(f'You have {score} points,Roll again? Keep/Roll', 'keep', 'roll')
        else:
            x = input.input_chk(f'Wow your doing great! Keep the {sum(scores_list)} points and end turn,'
                                f'or hold dice and continue to roll? Keep/Roll:', 'keep', 'roll')
        roll_again = True
        while roll_again:
            if x == 'keep':
                scores_list.append(score)
                turn = False
                break
            else:
                z = 1
                held = dice.hold(roll)
                scores_list.append(sc.turn_score(held))
                roll = dice.add_roll(6, len(held))
                score = sc.turn_score(roll)
                rollin = True
                while rollin:
                    if score == 0:
                        print(f'{roll} is a farkle!')
                        scores_list = []
                        roll_again = False
                        turn = False
                        break
                    if sc.all_dice_score_chk(roll):
                        scores_list.append(sc.turn_score(roll))
                        x = input.input_chk(f'All dice have scored keep {sum(scores_list)} '
                                            f'or risk and roll again? Roll/Keep', 'roll', 'keep')
                        if x == 'keep':
                            roll_again = False
                            turn = False
                            break
                        else:
                            roll_again = False
                            break

                    else:
                        k = len(roll)
                        held = dice.hold(roll)
                        scores_list.append(sc.turn_score(held))
                        x = input.input_chk(f'You scored! Keep the {sum(scores_list)} points and end turn,'
                                            f'or hold more dice and continue to roll? Keep/Roll:', 'keep', 'roll')
                        if x == 'keep':
                            roll_again = False
                            turn = False
                            break
                        else:
                            roll = dice.add_roll(k, len(held))
                            score = sc.turn_score(roll)
                            continue


print(sum(scores_list))
