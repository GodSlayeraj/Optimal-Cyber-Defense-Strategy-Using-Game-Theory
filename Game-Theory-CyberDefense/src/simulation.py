# simulation.py
import random
from model import def_payoff

def simulate_round(p,h,m):
    attacks = ["A1","A2","A3"]
    a = random.choice(attacks)
    return def_payoff(a,p,h,m)

def simulate(defense, rounds=10000):
    total = 0
    for _ in range(rounds):
        total += simulate_round(*defense)
    return total/rounds

if __name__ == "__main__":
    avg = simulate((2,1,1))
    print(f"Expected payoff after simulation: {round(avg,2)}")
