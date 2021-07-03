from random import randint
from score import Score

class Dice:

    def init_roll():
        init_dice_roll = []
        for r in range(0, 6):
            init_dice_roll.append(randint(1, 6))
        return init_dice_roll

    def add_roll(held):
        add_dice_roll = []
        for r in range(0, 6-len(held)):
            add_dice_roll.append(randint(1, 6))
        return add_dice_roll

    def hold(cur_roll_list):
        die_pot = cur_roll_list
        die_score = True
        while die_score:
            die_held = []
            die_select = True
            while die_select:
                try:
                    if die_pot == []:
                        print('All dice have been held!')
                        break
                    print(die_pot)
                    d = input("Please select the number of a die to keep or type Q to keep current held dice:")
                    if d.lower().strip() == "q":
                        die_select = False
                    else:
                        die_pot.remove(int(d))
                        die_held.append(int(d))
                except ValueError:
                    print("Number not in list!!! Please try again.")
                    continue
            if Score.all_dice_score_chk(die_held) and die_held != []:
                break
            else:
                print(f'Dice held {die_held} is empty or not all scoring please try again!')
                die_pot = die_pot + die_held
                continue

        return die_held


# x = Dice.init_roll()
# z = Dice.hold(x)
# print(z)