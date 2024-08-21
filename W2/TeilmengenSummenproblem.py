list = [3,34,55,12,5,2]



def calc (n):
    for i in list:
        if i > 9:
            list.remove(i)

    summenliste = []
    while sum(summenliste) != n:
        for i in list:
            summenliste.append(i)
            print(summenliste)
            if sum(summenliste) > n:
                summenliste.pop()
    if sum(summenliste) == n:
        return True
    else:
        return False

print(calc(9))


