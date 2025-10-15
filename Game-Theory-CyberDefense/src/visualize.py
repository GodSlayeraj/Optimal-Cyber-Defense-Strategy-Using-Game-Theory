# visualize.py
import matplotlib.pyplot as plt
import numpy as np
from model import def_payoff, COST

def best_defender_value_for_budget(B):
    best = None
    for p in range(3):
        for h in range(3):
            for m in range(3):
                cost = COST["P"]*p + COST["H"]*h + COST["M"]*m
                if cost <= B:
                    val = max(def_payoff(a,p,h,m) for a in ["A1","A2","A3"])
                    if (best is None) or (val > best):
                        best = val
    return best if best is not None else float("-inf")

def plot_budget_vs_loss(save_path=None):
    budgets = list(range(0, 13))
    exp_loss = []
    for B in budgets:
        v = best_defender_value_for_budget(B)
        exp_loss.append(-v if v != float("-inf") else None)
    fig = plt.figure()
    plt.plot(budgets, exp_loss, marker="o")
    plt.title("Budget vs Expected Loss")
    plt.xlabel("Budget")
    plt.ylabel("Expected Loss")
    plt.grid(True)
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    return fig

if __name__ == "__main__":
    plot_budget_vs_loss()
    plt.show()
