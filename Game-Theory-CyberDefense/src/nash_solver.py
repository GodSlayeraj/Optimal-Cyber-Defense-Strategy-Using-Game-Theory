# nash_solver.py
import numpy as np
from scipy.optimize import linprog
from model import def_payoff, COST
import itertools

BUDGET = 8

def feasible_configs():
    configs = []
    for p,h,m in itertools.product(range(3), repeat=3):
        c = COST["P"]*p + COST["H"]*h + COST["M"]*m
        if c <= BUDGET:
            configs.append((p,h,m))
    return configs

def payoff_matrix():
    d_strats = feasible_configs()
    a_strats = ["A1","A2","A3"]
    M = np.zeros((len(d_strats), len(a_strats)))
    for i, d in enumerate(d_strats):
        for j, a in enumerate(a_strats):
            M[i,j] = def_payoff(a,*d)
    return M, d_strats, a_strats

def nash_equilibrium():
    M, d_strats, a_strats = payoff_matrix()
    # Zero-sum assumption: maximize v s.t. x*M >= v
    m, n = M.shape
    c = np.zeros(m+1)
    c[-1] = -1
    A_ub = np.hstack([-M.T, np.ones((n,1))])
    b_ub = np.zeros(n)
    A_eq = np.zeros((1,m+1))
    A_eq[0,:m] = 1
    b_eq = [1]
    bounds = [(0,None)]*m + [(None,None)]
    res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=bounds, method="highs")
    if res.success:
        probs = res.x[:-1]
        v = -res.fun
        return probs/np.sum(probs), v, d_strats
    else:
        raise Exception("LP failed: " + str(res.message))

if __name__ == "__main__":
    p,v,d_strats = nash_equilibrium()
    print("Nash Defender Strategy:")
    for i,pv in enumerate(p):
        print(f" {d_strats[i]} -> {round(pv,3)}")
    print("Value of Game:", round(v,2))
