class Checkbook:
    """
    A simple checkbook class that allows users to deposit, withdraw, 
    and check their balance.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Parameters:
        amount (float): The amount to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook if funds are available.

        Parameters:
        amount (float): The amount to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompts the user to enter a valid numeric amount.
    
    Parameters:
    prompt (str): The message to display to the user.

    Returns:
    float: The valid numeric amount entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a positive amount.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")


def main():
    """
    Runs the checkbook program, allowing the user to deposit, withdraw, 
    check their balance, or exit.

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            print("Exiting the checkbook program.")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
