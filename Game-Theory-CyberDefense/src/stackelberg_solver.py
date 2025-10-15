# stackelberg_solver.py
from model import def_payoff, att_payoff, COST
import itertools

BUDGET = 8

def feasible_configs():
    for p,h,m in itertools.product(range(3), repeat=3):
        c = COST["P"]*p + COST["H"]*h + COST["M"]*m
        if c <= BUDGET:
            yield (p,h,m)

def stackelberg_solve():
    best = None
    for d in feasible_configs():
        attacker = max(["A1","A2","A3"], key=lambda a: att_payoff(a,*d))
        payoff = def_payoff(attacker, *d)
        if (best is None) or (payoff > best[0]):
            best = (payoff, d, attacker)
    return best

if __name__ == "__main__":
    payoff, defense, attack = stackelberg_solve()
    print(f"Optimal Defense (P,H,M): {defense}")
    print(f"Attacker Best Response: {attack}")
    print(f"Defender Payoff: {round(payoff,2)}")
