# author:   Bartosz Zbiegień
# date:     19.11.2020

def convert2rd(coord):
    x, y = coord

    return x + y


def convert2ld(coord):
    x, y = coord

    # return x + y//2 - 1

    if x > y:
        ldx = x - y
        ldy = 0
    else:
        ldx = 0
        ldy = y - x

    if ldx == 0:
        return 99 - ldy
    return ldx + 99


def is_not_check(queen_tab):
    x_tab = [False for i in range(100)]
    y_tab = [False for i in range(100)]
    ld_tab = [False for i in range(199)]
    rd_tab = [False for i in range(199)]

    for queen in queen_tab:
        x, y = queen

        if x_tab[x] or y_tab[y] or ld_tab[convert2ld(queen)] or rd_tab[convert2rd(queen)]:
            return False
        x_tab[x] = y_tab[y] = ld_tab[convert2ld(queen)] = rd_tab[convert2rd(queen)] = True

    return True


dane = [(5, 5), (4, 6)]

print(is_not_check(dane))
