class Score:

    def turn_die_tally(held_die):
        scoring_die = held_die
        die_tally = []
        for i in range(1, 7):
            x = 0
            for die in scoring_die:
                if die == i:
                    x += 1
            die_tally.append(x)
        return die_tally

    def turn_score(die_tally):
        tally_list = die_tally
        a = tally_list.count(1)
        b = tally_list.count(2)
        c = tally_list.count(3)
        x = tally_list.count(4)
        y = tally_list.count(5)
        z = tally_list.count(6)
        turn_score = 0
        if a == 6:
            turn_score += 1500
        if a < 6 and b < 3 and z < 1:
            turn_score += tally_list[0] * 100
            turn_score += tally_list[4] * 50
        if b == 3:
            turn_score += 1500
        if c == 1 and tally_list[0] == 3:
            turn_score += 1000
        if c == 1 and tally_list[0] != 3:
            turn_score += 100 * (tally_list.index(3) + 1)
        if c == 2:
            turn_score += 2500
        if x == 1 and tally_list[0] != 4:
            turn_score += 1000
        if x == 1 and tally_list[0] == 4:
            turn_score += 2000
        if y == 1 and a != 1 and b != 1:
            turn_score += 3000
        if y == 1 and a == 1:
            turn_score += 3100
        if y == 1 and b == 1:
            turn_score += 3050
        if z == 1:
            turn_score += 3500
        return turn_score


held_die = [3,3,3,3,3,1]
print(held_die)
die_tally = Score.turn_die_tally(held_die)
print(die_tally)
round_score = Score.turn_score(die_tally)
print(round_score)
