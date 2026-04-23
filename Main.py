import sys
STANDARD_DEDUCTION = 15750

def get_totals(prompt):
    total = 0
    print(prompt)
    while True:
        user_input = input("Enter value: ")

        if user_input.lower() == "done":
            break

        try:
            total += float(user_input)
        except ValueError:
            print("Invalid number, try again.")

    return total

def calculate_tax(agi):
    brackets = [
        (0, 11925, 0.10),
        (11925, 48475, 0.12),
        (48475, 103350, 0.22),
        (103350, 197300, 0.24),
        (197300, 250525, 0.32),
        (250525, 626350, 0.35),
        (626350, sys.maxsize, 0.37)
    ]

    total_tax = 0
    tax_results = []
    for start, end, rate in brackets:
        if agi <= start:
            tax = 0
        elif agi > end:
            tax = (end - start) * rate
        else:
            tax = (agi - start) * rate

        tax_results.append((rate, tax))
        total_tax += tax

    return total_tax, tax_results

def main():
    print("\nIncome Tax Estimator\n")

    deductions = get_totals("Enter your deductions or done")
    income = get_totals("Enter your income sources")

    if deductions < STANDARD_DEDUCTION:
        deductions = STANDARD_DEDUCTION

    agi = income - deductions
    
    if agi < 0:
        agi = 0

    total_tax, breakdown = calculate_tax(agi)

    print("\n Tax Breakdown")

    for rate, tax in breakdown:
        print(f"{int(rate * 100)}% bracket: ${tax:,.2f}")

    print(f"Total taxes owed: ${total_tax:,.2f}")

    if income > 0:
        print(f"Tax owed as a percentage of gross income: {total_tax / income * 100:.2f}%")

    if agi > 0:
        print(f"Tax owed as a percentage of adjusted gross income: {total_tax / agi * 100:.2f}%")
