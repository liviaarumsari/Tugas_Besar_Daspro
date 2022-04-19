
def LCG(N,S):               # linear congruential generator (LCG)
    a = 7**3
    M = 2**5-1

    def f(S):
        return (a*S) % M
    
    U = 0
    for i in range(N):
        S = f(S)
        U += (S/M)
    return U
