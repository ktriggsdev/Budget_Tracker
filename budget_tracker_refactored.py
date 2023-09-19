# Initialize variables:

exps = []

# Function to retrieve a name:
def get_name():
    print("please enter your name:")
    name = input("> ").lower()
    return name

# Function to get the currency type:
def get_currency():
    print("Are you using dollars (d) or pounds (p)?:")
    dollars_pounds = input("> ").lower().removesuffix("ounds").removesuffix("ollars")
    return dollars_pounds

# Function to get the income:
def get_income():
    print("How much income do you have? Enter it in price format")
    income = input("> ").removeprefix("$").removeprefix("£").removesuffix("USD").removesuffix("GBP")
    if income == "":
        print("Error: not a valid value")
        return None
    else:
        return float(income)

# Function to get the expenses:
def get_expenses():
    print("Enter your expenses in price format:")
    while True:
        exp = input("> ").removeprefix("$").removeprefix("£").removesuffix("USD").removesuffix("GBP")
        if exp == "":
            break
        else:
            exps.append(float(exp))
    return exps

# Function to get the total expenses:
def get_total_exp():
    total_exp = sum(exps)
    return total_exp

# Function to get the remaining budget:
def get_remaining_bgt(total_exp):
    remaining_bgt = income - total_exp
    return remaining_bgt

# Function to display the results:
def display_results(dollars_pounds, exps, remaining_bgt, total_exp):
    if dollars_pounds == "p":
        print(f"Your income is: £{income:.2f} GBP")
        exps = str(exps)
        print(f"Your expenses list is: {exps}")
        print(f"Your total expenses are: £{total_exp:.2f} GBP")
        print(f"Your remaining budget is: £{remaining_bgt:.2f} GBP")
    elif dollars_pounds == "d":
        print(f"Your income is: ${income:.2f} USD")
        exps = str(exps)
        print(f"Your expenses list is: {exps}")
        print(f"Your total expenses are: ${total_exp:.2f} USD")
        print(f"Your remaining budget is: ${remaining_bgt:.2f} USD")

# Main function:
def main():
    # Get the user's name:
    name = get_name()

    # Display the docstring:
    docstring = f"""
    Hello {name}, this is a simple program to calculate your expenses
    and see your budget

    To use this program:

    first choose your model type: dollars or pounds

    next enter your income

    then enter your expenses one by one

    The program will now calculate your budget and will then display it to you
    """

    print(docstring)

    # Get the user's currency type:
    dollars_pounds = get_currency()

    # Get the user's income:
    global income
    income = get_income()
    if income is None:
        return

    # Get the user's expenses:
    exps = get_expenses()

    # Calculate the total expenses:
    total_exp = get_total_exp()

    # Calculate the remaining budget:
    remaining_bgt = get_remaining_bgt(total_exp)

    # Display the results:
    display_results(dollars_pounds, exps, remaining_bgt, total_exp)

if __name__ == "__main__":
    main()