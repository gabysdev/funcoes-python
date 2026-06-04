def fatorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res    

if __name__ == "__main__":
    print(fatorial(5))