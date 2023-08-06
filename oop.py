class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts

class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def get_balance(self):
        return self.balance

# Sample usage:
if __name__ == "__main__":
    # Create customers
    customer1 = Customer("John Doe", "123 Main St", "555-1234")
    customer2 = Customer("Jane Smith", "456 Oak Ave", "555-5678")

    # Create accounts
    account1 = Account("001", 1000)
    account2 = Account("002", 500)

    # Add accounts to customers
    customer1.add_account(account1)
    customer2.add_account(account2)

    # Perform operations on accounts
    account1.deposit(1250)
    account1.withdraw(680)
    account2.deposit(600)
    account2.withdraw(1200)

    # Get account balances
    print(f"Account {account1.account_number} balance: ${account1.get_balance()}")
    print(f"Account {account2.account_number} balance: ${account2.get_balance()}")