def check(tab):
    for het1 in tab:
        for het2 in tab:
            if het1 == het2:
                continue

            if het1[0] == het2[0] or het1[1] == het2[1]:
                return False

            a = (het1[1] - het2[1])/(het1[0]-het2[0])

            if a == 1.0 or a == -1.0:
                return False
    
    return True


print(check([(1,1), (3, 4), (1, 6)]))