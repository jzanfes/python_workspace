
class PlayerInput:

    def input_chk(prompt, cond1, cond2):
        z = prompt + ':'
        entry_chk = True
        while entry_chk:
            y = input(z)
            x = y.strip().lower()
            if x == cond1 or x == cond2:
                break
            else:
                continue
        return x

#f = PlayerInput.input_chk("what age are you? Teen or Adult", "teen", "adult")
#print(f)