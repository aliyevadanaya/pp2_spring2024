def ok(s = input()):
    s2 = ""
    msv = s.split()
    for i in range(len(msv)-1, -1, -1):
        s2 += msv[i] + " "
    return s2
        
print(ok())
    