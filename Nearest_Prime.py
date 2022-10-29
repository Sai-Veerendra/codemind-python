t=int(input())
for i in range(t):
    def is_prime(num):
        if num<2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    def run_loop_till_prime(n,x): # n=8, x = -1
        while is_prime(n) == False: #is_prime(7)
            n+=x #7
        return n #n=7
    n=int(input())
    pp= run_loop_till_prime(n, -1) #7
    np= run_loop_till_prime(n, 1) #11
    
    if n-pp <= np-n:
        print(pp)
    else:
        print(np)