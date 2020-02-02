def on_rahulik(arvamus1, arvamus2, erinevus):
    if arvamus1 * arvamus2 >= 0:
        return True
    if abs(arvamus1 - arvamus2) > erinevus:
        return False
    return True


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0

    for i in range(len(arvamused)-1):
        if on_rahulik(arvamused[i], arvamused[i+1], lubatud_erinevus) == False:
            dissonantsid += 1

    return dissonantsid
