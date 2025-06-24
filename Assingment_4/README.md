## Banking System Implementation - README

### Project Overview
This Python banking system implements a robust class hierarchy for bank accounts with core banking operations, inheritance, and customer management. The system includes:
- **Account Types**: Base `BankAccount`, interest-earning `SavingsAccount`, and overdraft-enabled `CheckingAccount`
- **Customer Management**: Track multiple accounts per customer with balance transfers
- **Demo Script**: Ready-to-run example of banking operations

---

## Key Features

### 🏦 Account Classes
| Class | Key Features |
|-------|-------------|
| `BankAccount` | Core banking operations, balance validation, operator overloading (`+`) |
| `SavingsAccount` | Interest application with `apply_interest()` method |
| `CheckingAccount` | Overdraft protection with custom withdrawal rules |

### 👤 Customer Management
- Track multiple accounts per customer
- Calculate total balance across accounts
- Transfer funds between accounts

### 🔒 Security & Validation
- Private balance attribute with property accessors
- Transaction validation (non-negative amounts, sufficient funds)
- Overdraft limit enforcement

### ✨ Special Features
- Operator overloading (`account1 + account2`)
- Polymorphic behavior through inheritance
- Clean string representations (`__str__` and `__repr__`)

---

## Class Documentation

### `BankAccount`
**Core account functionality**
```python
def deposit(self, amount: float)  # Add funds
def withdraw(self, amount: float)  # Remove funds
@property balance  # Get current balance
@balance.setter  # Set balance (with validation)
```

### `SavingsAccount(BankAccount)`
**Interest-earning account**
```python
def apply_interest(self)  # Calculate and deposit interest
```

### `CheckingAccount(BankAccount)`
**Account with overdraft protection**
```python
def withdraw(self, amount: float)  # Custom withdrawal with overdraft
@property overdraft_limit  # Get/set overdraft limit
```

### `Customer`
**Account management for users**
```python
def add_account(self, account)  # Link account to customer
def total_balance(self)  # Sum all account balances
def transfer(self, from_acc, to_acc, amount)  # Move funds between accounts
```

---

## Demo Execution
The included demo script demonstrates:
1. Account creation (savings and checking)
2. Interest application
3. Overdraft withdrawal
4. Account combination using `+` operator
5. Customer management and fund transfers

**Run the demo:**
```bash
python banking.py
```

**Expected Output:**
```
BankAccount(owner=Ayushmaan, balance=1050.00)
BankAccount(owner=Madhav, balance=-100.00)
BankAccount(owner='Ayushmaan & Madhav', balance=950.00)
Total balance for Raghav: 950.0
Owner: Ayushmaan, Balance: 950.0
Owner: Madhav, Balance: 0.0
Object does not conform to required interface
BankAccount(owner=Ayushmaan, balance=950.00)
BankAccount(owner=Madhav, balance=0.00)
```

---

## Usage Example
```python
# Create specialized accounts
savings = SavingsAccount("Alice", 5000, 0.03)
checking = CheckingAccount("Bob", 1000, 500)

# Perform banking operations
savings.apply_interest()          # Adds interest
checking.withdraw(1300)           # Uses overdraft

# Manage customer accounts
customer = Customer("Charlie")
customer.add_account(savings)
customer.add_account(checking)
customer.transfer(savings, checking, 200)  # Transfer between accounts
```

---

## Design Principles
1. **Encapsulation**: Private balance with controlled access
2. **Inheritance**: Specialized account types extend base functionality
3. **Polymorphism**: Shared interface with account-specific behaviors
4. **Operator Overloading**: Intuitive account combination with `+`
5. **Error Handling**: Validated transactions with meaningful exceptions

This implementation provides a foundation for banking operations with extensible architecture for additional features.
