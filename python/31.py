#31. **Simple Interest Function:** Write `calculate_interest(principal, rate, time)` that returns $P \times R \times T / 100$.

def si(principal,rate,time):
    sim_int=(principal*rate*time)/100
    
    return sim_int
print(si(int(input("principal amount : ")),int(input("rate : ")),int(input("time : "))))

    
