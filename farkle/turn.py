from dice import Dice
from score import Score

scores_list = []
turn = True
while turn:
    roll = Dice.init_roll()
    scores_list.append(Score.turn_score(roll))
    if scores_list[-1] == 0:
        print(f'{roll} is a farkle!')
        break
    else:
        x = input(f'Would you like to keep the {sum(scores_list)} points or hold dice and continue to roll? Keep/Roll:')
        roll_again = True
        while roll_again:
            try:
                if x.strip().upper() == 'KEEP':
                    scores_list.append(score)
                    roll_again = False
                if x.strip().upper() == 'ROLL':
                    rollin = True
                    while rollin:
                        held = Dice.hold(roll)
                        add_roll = Dice.add_roll(held)
                        score = Score.turn_score(add_roll)
                        if len(held) == 6:
                            break
                        else:
                            add_roll = Dice.add_roll(held)
                            score = Score.turn_score(add_roll)
                            scores_list.append(score)



            except:
                continue



print(score)