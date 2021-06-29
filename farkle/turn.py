from dice import Dice
from score import Score
import input

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
        x = input.input_chk("All dice scored, would you like to roll again? y/n",'y','n')
        if x == 'y':
            continue
        else:
            Turn = False

    else:
        if z == 0:
            x = input.input_chk(f'You have {score} points would you like to keep or roLL again Keep/Roll','keep','roll')
        else:
            x = input.input_chk(f'Wow your doing great! Keep the {sum(scores_list)} points and end turn,'
                    f'or hold dice and continue to roll? Keep/Roll:','keep','roll')
        roll_again = True
        while roll_again:
            if x == 'keep':
                scores_list.append(score)
                turn = False
                break
            if x == 'roll':
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


