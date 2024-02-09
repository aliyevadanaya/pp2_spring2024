import math
def filter_primes(msv):
    for i in msv:
        a = i
        for i in range(2, int(math.sqrt(a))+1):
            if a%i==0:
                msv.remove(a)
                break
        if a<2: 
            msv.remove(a)
    return msv


if __name__=="__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    print(filter_primes(a))

            
            
            
    