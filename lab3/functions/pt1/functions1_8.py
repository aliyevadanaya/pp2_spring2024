def spy_game(msv):
    id = len(msv) - 1 - msv[::-1].index(7)
    return msv[:id].count(0) >= 2
  

spisok = [0, 4, 5, 0, 0, 6, 0, 7, 8]
print(spy_game(spisok))
