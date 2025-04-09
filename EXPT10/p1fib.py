def fib(n):
    fst = 0
    snd = 1
    for i in range(0,n):
        print(fst,end=" ")
        sm = fst + snd
        fst = snd
        snd = sm

fib(20)