def like_set(msv):
    newlist = []
    for i in range(0, len(msv)):
        if msv[i] in newlist:
            continue
        else:
            newlist.append(msv[i])
    return newlist

a = [1, 2, 2, 3, 4, 5, 5, 4, 6]
print(like_set(a))
