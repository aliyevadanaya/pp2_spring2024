import itertools
def perm(s = input()):
    l = list(itertools.permutations(s))
    for i in l:
        print(''.join(i))
    
        
if __name__=="__main__":    
    perm()
