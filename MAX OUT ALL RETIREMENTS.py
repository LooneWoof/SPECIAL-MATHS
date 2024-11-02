# Constants for the simulation
initial_401k_limit = 23500       # Initial 401(k) contribution limit for 2025
initial_roth_ira_limit = 7000    # Initial Roth IRA contribution limit for 2025
initial_hsa_limit = 4300         # Initial HSA contribution limit for 2025
annual_401k_increase = 500       # Yearly increase in 401(k) contribution limit
annual_roth_ira_increase = 500   # Yearly increase in Roth IRA contribution limit
annual_hsa_increase = 500        # Yearly increase in HSA contribution limit
employer_match_rate = 0.06       # 6% employer match for 401(k)
growth_rate = 0.08               # Annual growth rate of 8%
target_net_worth = 15000000      # Target net worth of $15 million
year = 2025                      # Starting year

# Initialize account balances and net worth
net_worth = 0
account_balances = {"401k": 0, "Roth IRA": 0, "HSA": 0}
current_401k_limit = initial_401k_limit
current_roth_ira_limit = initial_roth_ira_limit
current_hsa_limit = initial_hsa_limit
years = 0

# Simulation loop
while net_worth < target_net_worth:
    # Calculate total 401(k) contributions with employer match
    employee_401k_contribution = current_401k_limit
    employer_401k_match = employee_401k_contribution * employer_match_rate
    total_401k_contribution = employee_401k_contribution + employer_401k_match

    # Update balances with contributions
    account_balances["401k"] += total_401k_contribution
    account_balances["Roth IRA"] += current_roth_ira_limit
    account_balances["HSA"] += current_hsa_limit

    # Apply annual growth to each account
    for account in account_balances:
        account_balances[account] *= (1 + growth_rate)

    # Update net worth
    net_worth = sum(account_balances.values())

    # Increment year and update contributions for the next year
    years += 1
    current_401k_limit += annual_401k_increase
    current_roth_ira_limit += annual_roth_ira_increase
    current_hsa_limit += annual_hsa_increase

# Calculate final year when the target is reached
final_year = year + years
print(f"It would take until {final_year} ({years} years from 2025) to reach $15 million.")
