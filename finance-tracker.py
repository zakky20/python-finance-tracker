import datetime

class Transaction:
    """A class to represent a financial transaction."""

    def __init__(self, amount, transaction_type, description=""):
        self.amount = amount
        self.transaction_type = transaction_type # income or expense
        self.description = description
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.title()}: {self.amount} | {self.description}"

class Account:
    """A class to represent the user's account, storing income, expenses, and balance."""

    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, description=""):
        """Adds an income transaction."""
        income = Transaction(amount, 'income', description)
        self.transactions.append(income)
        self.balance += amount
        print(f"Income of {amount} added. Current balance: {self.balance}")

    def add_expense(self, amount, description=""):
        """Adds an expense transaction."""
        if amount > self.balance:
            print("Not enough balance for this expense.")
            return
        expense = Transaction(amount, 'expense', description)
        self.transactions.append(expense)
        self.balance -= amount
        print(f"Expense of {amount} deducted. Current balance: {self.balance}")

    def get_balance(self):
        """Returns a list of all transactions."""
        return self.balance

    def get_transaction_history(self):
        """Returns a list of all transactions."""
        if not self.transactions:
            return "No transactions available."
        return "\n".join([str(t) for t in self.transaction])

class FinanceManager:
    """A class to handle user interaction and manage the finance system."""

    def __init__(self):
        self.account = Account()

    def show_menu(self):
        """Displays the user menu."""
        menu = """
        Personal Finance Manager Menu:
        1. Add Income
        2. Add Expense
        3. View Transaction History
        4. View Balance
        5. Exit
        """
        print(menu)

    def add_income(self):
        """Prompts user to add an income transaction."""
        try:
            amount = float(input("Enter income amount:"))
            description = input("Enter income description (optional):")
            self.account.add_income(amount, description)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def add_expense(self):
            """Prompts user to add an expense transaction."""
            try:
                amount = float(input("Enter expense amount:"))
                description = input("Enter expense description (optional):")
                self.account.add_income(amount, description)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_transaction_history(self):
        """Displays the user transaction history."""
        print("\nTransaction History:")
        print(self.account.get_transaction_history())

    def view_balance(self):
        """Displays the user's current history."""
        print(f"Current Balance: {self.account.get_balance()}")

    def run(self):
        """Runs the finance manager."""
        while True:
            self.show_menu()
            choice = input("Select an option: ")
            if choice == '1':
                self.add_income()
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.view_transaction_history()
            elif choice == '4':
                self.view_balance()
            elif choice == '5':
                print("Exiting. Thank you for using the Personal Finance Manager.")
                break
            else:
                print("Invalid option. Please choose a valid option.")

# Main program
if __name__ == "__main__":
    finance_manager = FinanceManager()
    finance_manager.run()

