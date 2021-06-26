from dice import Dice
from score import Score

scores_list = []
turn = True
z = 0
while turn:
    roll = Dice.init_roll()
    print(roll)
    score = Score.turn_score(roll)
    print(f'Roll score {score}!')
    if score == 0:
        print(f'{roll} Farkle!!')
        scores_list = []
        break
    elif Score.all_dice_score_chk(roll):
        scores_list.append(score)
        entry_chk = True
        while entry_chk:
            y = input('All dice scored!!! Would you like to roll again y/n')
            x = y.strip().lower()
            if x == 'y' or x == 'n':
                break
            else:
                continue


    else:
        if z == 0:
            entry_chk = True
            while entry_chk:
                x = input(f'Would you like to keep the {score}'
                    f' points or hold dice and continue to roll? Keep/Roll:')
                if x.strip().upper() == 'KEEP' or x.strip().upper() == 'ROLL':
                    entry_chk = False
                else:
                    continue

        else:
            entry_chk = True
            while entry_chk:
                x = input(f'Wow your doing great! Keep the {sum(scores_list)} points and end turn,'
                    f'or hold dice and continue to roll? Keep/Roll:')
                if x.strip().upper() == 'KEEP' or x.strip().upper() == 'ROLL':
                    entry_chk = False
                else:
                    continue
        roll_again = True
        while roll_again:
            if x.strip().upper() == 'KEEP':
                z = 1
                scores_list.append(score)
                turn = False
                break
            if x.strip().upper() == 'ROLL':
                z = 1
                rollin = True
                while rollin:
                    y = len(roll)
                    held = Dice.hold(roll)
                    x = len(held)
                    if x == y:
                        score = Score.turn_score(held)
                        roll_again = False
                        break
                    if score == 0:
                        print(f'{roll} is a farkle!')
                        scores_list = []
                        roll_again = False
                        turn = False
                        break
                    else:
                        roll = Dice.add_roll(held)
                        score = Score.turn_score(roll)
                        held = Dice.hold(roll)
                        score = Score.turn_score(held)
                        scores_list.append(score)
                        continue
            else:
                break

print(sum(scores_list))




