def fibDynamic(n,memo={}):
    global Dy
    Dy +=1
    if n==0 or n==1:
        return 1
    if n not in memo:
        result = fibDynamic(n-1,memo) + fibDynamic(n-2,memo)
        memo[n] = result
        return result
    else:
        return memo[n]
def fib(n):
    global fibn
    fibn+=1
    if n==0 or n==1:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
        return result

Dy,fibn = 0,0
print(fibDynamic(35),'\tTotal calling in fibDynamic: ',Dy)
print(fib(12),'\tTotal calling in fibNormal: ',fibn)





