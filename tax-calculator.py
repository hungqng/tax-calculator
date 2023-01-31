def calculate_tax(income: float, tax_rate: float) -> float:
    return income / tax_rate

if __name__ == "__main__":
    income = float(input("Enter your income: "))
    tax_rate = float(input("Enter the tax rate (as a percentage): "))
    tax = calculate_tax(income, tax_rate)
    print(f"Your tax is: {tax}")
