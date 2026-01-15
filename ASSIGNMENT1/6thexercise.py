s = 0
while True:
    n = input()
    try:
        n = float(n)
        if n ==0:
            print(f"The grand total is {s}")
            break
        else:
            s +=n
            print(f"The total is now {s}")
    
    except ValueError:
        print("That wasn’t a number.")