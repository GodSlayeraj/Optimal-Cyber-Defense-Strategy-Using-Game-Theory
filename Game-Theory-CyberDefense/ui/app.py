# ui/app.py
import sys, os
# Ensure src is importable when running `streamlit run ui/app.py`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import streamlit as st
from stackelberg_solver import stackelberg_solve, BUDGET
from visualize import plot_budget_vs_loss

st.title("🛡️ Cyber Defense Game Theory Simulator")
st.caption("Stackelberg–Nash model for optimal defense under limited budget")

st.sidebar.header("Settings")
budget = st.sidebar.slider("Budget (units)", min_value=0, max_value=12, value=BUDGET, step=1)
st.sidebar.write("Adjust code constants in `src/` for deeper changes.")

run = st.button("Run Stackelberg Model")
if run:
    payoff, defense, attack = stackelberg_solve()
    st.success(f"Optimal Defense (P,H,M): {defense}")
    st.info(f"Attacker’s Best Response: {attack}")
    st.warning(f"Defender Payoff: {round(payoff,2)}")


st.subheader("📈 Budget vs Expected Loss")
fig = plot_budget_vs_loss(save_path=None)
st.pyplot(fig)
