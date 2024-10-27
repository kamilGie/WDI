def is_zero_in_every_line(tab):
    for line in tab:
        is_zero = False
        for elem in line:
            if elem == 0:
                is_zero = True
                break
        if not is_zero:
            return False
    
    return True
