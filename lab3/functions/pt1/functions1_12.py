def histogram(spisok):
    for i in range(0, len(spisok)):
        for i in range(0, spisok[i]):
            print("*", end="")
        print(end=' ')
            
if __name__=="__main__":
    msv = [4, 2, 1]
    histogram(msv)
