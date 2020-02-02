def on_rahulik(arvamus1, arvamus2, erinevus):
    if arvamus1 * arvamus2 >= 0:
        return True
    if abs(arvamus1 - arvamus2) > erinevus:
        return False
    return True


def dissonandid(arvamused, lubatud_erinevus):
    erilased = []

    for i in range(len(arvamused)-1):
        if on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus) == False:
            erilased.append((i, i+1))

    return erilased
