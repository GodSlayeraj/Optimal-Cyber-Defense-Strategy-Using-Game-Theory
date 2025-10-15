# model.py
import math

# Base probabilities and parameters
BASE = {"A1": 0.7, "A2": 0.6, "A3": 0.5}
LOSS = {"A1": 50, "A2": 120, "A3": 80}
VAL = {"A1": 60, "A2": 150, "A3": 90}
EFFORT = {"A1": 10, "A2": 15, "A3": 12}
ALPHA_P, ALPHA_H, ALPHA_M = 0.6, 0.7, 0.65
COST = {"P": 3, "H": 2, "M": 2}

def prob(a, p, h, m):
    if a == "A1":
        return BASE[a]*(ALPHA_P**p)*(ALPHA_H**h)
    if a == "A2":
        return BASE[a]*(ALPHA_P**p)
    if a == "A3":
        return BASE[a]*(ALPHA_H**h)

def def_payoff(a, p, h, m):
    pr = prob(a,p,h,m)
    realized = LOSS[a]*(ALPHA_M**m)
    cost = COST["P"]*p + COST["H"]*h + COST["M"]*m
    return -(pr*realized) - cost

def att_payoff(a, p, h, m):
    pr = prob(a,p,h,m)
    return pr*VAL[a] - EFFORT[a]
