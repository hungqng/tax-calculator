# define tax brackets and rates for 2022
tax_brackets = {
    10275: 0.10,
    41775: 0.12,
    89075: 0.22,
    170050: 0.24,
    215950: 0.32,
    539900: 0.35,
    float('inf'): 0.37
}

income = float(input("Enter your taxable income: $"))
state_tax = float(input("Enter your state income tax rate (as a decimal): "))

# calculate federal income tax
tax = 0
prev_bracket = 0
for bracket, rate in tax_brackets.items():
    if income > bracket:
        tax += (bracket - prev_bracket) * rate
    else:
        tax += (income - prev_bracket) * rate
        break
    prev_bracket = bracket

# calculate state income tax
state_income_tax = income * state_tax

# calculate total tax and net income
total_tax = tax + state_income_tax
net_income = income - total_tax

print(f"State income tax: ${state_income_tax:,.2f}")
print(f"Total tax: ${total_tax:,.2f}")
print(f"Net income after tax: ${net_income:,.2f}")