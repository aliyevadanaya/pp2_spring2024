l = [1, 3, 1, 2, 2, 3]
for i in range(0, len(l)):
    for j in range(i+1, len(l)):
        if l[i]==l[j]:
            print(l[i])
    