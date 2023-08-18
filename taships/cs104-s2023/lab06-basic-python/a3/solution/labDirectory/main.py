'''
    Functions and Memoization
'''

from analyse import analyser

# factorial
def factorial(lut, calls, n):
    calls.setdefault(n,0)
    calls[n] += 1
    if n in lut:
        return lut[n]
    if n == 0:
        lut[n] = 1
    else:
        lut[n] = n * factorial(lut,calls,n - 1)
    return lut[n]

# fibonacci function
def fibonacci(lut, calls, n):
    calls.setdefault(n,0)
    calls[n] += 1
    if n in lut:
        return lut[n]
    if n <= 1:
        lut[n] = n
    else:
        lut[n] = fibonacci(lut,calls,n - 1) + fibonacci(lut,calls,n - 2)
    return lut[n]

# nCr function
def nCr(lut, calls, n, r):
    calls.setdefault((n,r),0)
    calls[(n,r)] += 1
    if (n,r) in lut:
        return lut[(n,r)]
    if r == 0:
        lut[(n,r)] = 1
    elif n == 0:
        lut[(n,r)] = 0
    else:
        lut[(n,r)] = nCr(lut,calls,n - 1,r) + nCr(lut,calls,n - 1,r - 1)
    return lut[(n,r)]

# ackermann function
def ackermann(lut, calls, m, n):
    calls.setdefault((m,n),0)
    calls[(m,n)] += 1
    if (m,n) in lut:
        return lut[(m,n)]
    if m == 0:
        lut[(m,n)] = n + 1
    if m > 0 and n == 0:
        lut[(m,n)] = ackermann(lut,calls,m - 1,1)
    if m > 0 and n > 0:
        lut[(m, n)] = ackermann(lut,calls,m - 1,ackermann(lut, calls, m, n - 1))
    return lut[(m,n)]

if __name__ == '__main__':

    # as before, you can edit this main function as you want
    # sample calls have been placed here
    analyser(factorial,10)
    analyser(fibonacci,40)
    analyser(nCr,13,4)
    analyser(ackermann,3,5)
