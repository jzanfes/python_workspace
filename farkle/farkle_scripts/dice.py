from random import randint

class Dice:


    def init_roll():
        init_dice_roll = []
        for r in range(0, 6):
            init_dice_roll.append(randint(1, 6))
        return init_dice_roll

    def add_roll(x):
        add_dice_roll = []
        for r in range(0, x):
            add_dice_roll.append(randint(1, 6))
        return add_dice_roll

    def hold(cur_roll_list):
        die_held = []
        die_pot = cur_roll_list
        die_select = True
        while die_select:
            try:
                if die_pot == []:
                    die_select = False
                print(die_pot)
                d = input("Please select the number of a die to keep or type Q to quit:")
                if d.lower().strip() == "q":
                    die_select = False
                if die_held == []:
                    die_select = False
                else:
                    die_pot.remove(int(d))
                    die_held.append(int(d))
            except ValueError:
                print("Number not in list!!! Please try again.")
                continue
        return die_held

