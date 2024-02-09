def solve(numheads, numlegs):
    chicken = 2*numheads - (numlegs/2)
    rat = numheads - chicken
    return chicken, rat
#chicken+rat = numheads
#2chicken+4rat=numlegs

if __name__=="__main__":
    