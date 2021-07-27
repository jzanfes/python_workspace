from random import randint
import score

def init_roll():
    init_dice_roll = []
    for r in range(0, 6):
        init_dice_roll.append(randint(1, 6))
    return init_dice_roll

def add_roll(roll_num, held_num):
    add_dice_roll = []
    for r in range(0, roll_num - held_num):
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
                print(f'Dice that can be held {die_pot}')
                d = input("Please select the number of a die to Hold or type 'K' to keep current held dice:")
                if d.lower().strip() == "k":
                    die_select = False
                else:
                    die_pot.remove(int(d))
                    print(f'Die that may be held.   {die_pot}')
                    die_held.append(int(d))
                    print(f'Current die being held. {die_held}')
            except ValueError:
                print("Number not in list!!! Please try again.")
                continue
        if score.all_dice_score_chk(die_held) and die_held != []:
            break
        else:
            print(f'Dice held {die_held} is empty or not all scoring please try again!')
            die_pot = die_pot + die_held
            continue

    return die_held

# x = add_roll(4,1)
# print(x)
# x = Dice.init_roll()
# z = Dice.hold(x)
# print(z)