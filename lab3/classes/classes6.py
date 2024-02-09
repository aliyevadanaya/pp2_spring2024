f = lambda x : (len([i for i in range(2, x) if x%i==0])==0 and x>1)
nums = [1, 2, 3, 4, -5, 6, 7, 8] 
l = list(filter(f, nums)) 
print(l)

