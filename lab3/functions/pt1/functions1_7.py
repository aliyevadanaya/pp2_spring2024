def has_33(msv):
    for i in range(0, len(msv)-1):
        if msv[i]==3 and msv[i+1]==3:
            return True
    return False
        
a = [0, 3, 3, 2, 3]
print(has_33(a))