def facNums(x):
    factors = []
    for i in range(1, x):
        if(x % i == 0):
            factors.append(i);
    return(factors)

def sumFacs(x):
    return(sum(x))

def perNums(x):
    if(sumFacs(facNums(x))==x):
        return(True)
    else:
        return(False)

for i in range(0,1000):
    if(perNums(i)):
        print(str(i) + " is a perfect number")