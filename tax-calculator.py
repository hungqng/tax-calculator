import math

def calculate_joint_brackets(single_brackets):
    joint_brackets = []
    for threshold, rate in single_brackets:
        if math.isinf(threshold):
            joint_brackets.append((threshold, rate))
        else:
            joint_brackets.append((threshold * 2, rate))
    return joint_brackets

def get_tax_rate(year, income, filing_status):
    single_brackets = {
        2022: [(10275, 0.10), (41775, 0.12), (89075, 0.22), (170050, 0.24), (215950, 0.32), (539900, 0.35), (math.inf, 0.37)],
        2023: [(11000, 0.10), (44725, 0.12), (95375, 0.22), (182100, 0.24), (231250, 0.32), (578125, 0.35), (math.inf, 0.37)],
        2024: [(11600, 0.10), (47150, 0.12), (100525, 0.22), (191950, 0.24), (243725, 0.32), (609350, 0.35), (math.inf, 0.37)]
        # Add more years and corresponding single tax brackets as needed
    }

    joint_brackets = calculate_joint_brackets(single_brackets[year])

    brackets = single_brackets if filing_status == 'single' else joint_brackets
    
    for i, (threshold, rate) in enumerate(brackets):
        if rate == 0.35 and filing_status == 'joint':
            single_income_threshold = [bracket[0] for bracket in single_brackets[year] if bracket[1] == 0.35][0]
            adjusted_threshold = single_income_threshold * 1.2
            if income <= adjusted_threshold:
                # Update joint bracket threshold at 35% rate
                joint_brackets[i] = (adjusted_threshold, rate)
                return rate
        elif income <= threshold:
            return rate
        
def calculate_tax(income, tax_rate):
    return income * tax_rate

def main():
    year = int(input("Enter tax year number: "))
    income = float(input("Enter your income: "))
    filing_status = input("Are you filing single or joint? (single/joint): ").lower()

    tax_rate = get_tax_rate(year, income, filing_status)

    has_state_tax = input("Do you have state income tax? (yes/no): ").lower()
    if has_state_tax == 'yes':
        state_tax_rate = float(input("Enter your state income tax rate: "))
    else:
        state_tax_rate = 0.0

    federal_tax = calculate_tax(income, tax_rate)

    state_tax = calculate_tax(income, state_tax_rate)

    total_tax = federal_tax + state_tax

    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"State Tax: ${state_tax:.2f}")
    print(f"Total Tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()
