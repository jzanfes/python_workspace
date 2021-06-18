class Score:

    def turn_score(held_die):
        scoring_die = held_die
        die_tally = []
        for i in range(1, 7):
            x = 0
            for die in scoring_die:
                if die == i:
                    x += 1
            die_tally.append(x)

        a = die_tally.count(1)
        b = die_tally.count(2)
        c = die_tally.count(3)
        x = die_tally.count(4)
        y = die_tally.count(5)
        z = die_tally.count(6)
        turn_score = 0
        if a == 6:
            turn_score += 1500
        if a != 6 and b != 3 and c != 2 and die_tally[0] != 4 and die_tally[0] != 5\
                and die_tally[0] != 6:
            turn_score += die_tally[0] * 100
        if a != 6 and b != 3 and c != 2 and die_tally[4] != 4 and die_tally[4] != 5\
                and die_tally[4] != 6:
            turn_score += die_tally[4] * 50
        if b == 3:
            turn_score += 1500
        if c == 1 and die_tally[0] == 3:
            turn_score += 1000
        if c == 1 and die_tally[0] != 3:
            turn_score += 100 * (die_tally.index(3) + 1)
        if c == 2:
            turn_score += 2500
        if x == 1 and die_tally[0] != 4:
            turn_score += 1000
        if x == 1 and die_tally[0] == 4:
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

held_die = [4,4,4,4,1,1]
turn_score = Score.turn_score(held_die)
print(turn_score)
