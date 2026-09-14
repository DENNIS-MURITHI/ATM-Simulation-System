# Python ATM Banking System

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

## 📋 Overview

A secure, console-based Automated Teller Machine (ATM) simulation built with Python. This educational project demonstrates fundamental banking operations and core programming concepts including authentication, transaction processing, and account management.

Perfect for:
- Learning Python fundamentals
- Understanding banking system architecture
- Practicing control flow and conditional logic
- Exploring account management principles

---

## ✨ Features

### 🔐 Security
- **PIN Authentication**: Secure account access with predefined PIN verification
- **Access Control**: Unauthorized attempts are blocked with error messaging

### 💰 Core Banking Operations
- **Balance Inquiry**: Check current account balance instantly
- **Cash Withdrawal**: Withdraw funds with real-time balance validation
- **Deposit Funds**: Add money to account with immediate balance update
- **Graceful Exit**: Safely terminate the session

### 📊 Transaction Validation
- Automatic balance verification before withdrawal
- Prevention of overdraft transactions
- Real-time balance confirmation after each operation
- Clear error messages for invalid operations

---

## 🛠 Technical Stack

| Component | Details |
|-----------|---------|
| **Language** | Python 3.x |
| **Environment** | Console/Terminal |
| **Architecture** | Procedural |
| **Dependencies** | None (Built-in Python only) |

---

## 📦 Installation

### Prerequisites
- Python 3.x installed on your system
- Basic terminal/command line knowledge

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/python-atm-banking-system.git
   cd python-atm-banking-system
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **Run the Program**
   ```bash
   python atm.py
   ```

---

## 🚀 Usage Guide

### Starting the Application
Execute the program with:
```bash
python atm.py
```

### Interactive Menu Flow

```
Step 1: Enter PIN
├─ Correct PIN (1234) → Access Granted
└─ Incorrect PIN → Access Denied

Step 2: Select Operation
├─ Option 1: Check Balance
├─ Option 2: Withdraw Money
├─ Option 3: Deposit Money
└─ Option 4: Exit Program

Step 3: Perform Transaction
├─ Complete operation
└─ View updated balance

Step 4: Continue or Exit
```

### Example Walkthrough

```
=============================
          Dennis ATM         
=============================

Enter your pin: 1234

ATM Menu
1 check the balance
2 Withdraw money
3 Deposit Money
4 Exit

Select an option from the menu: 1
your balance is 40000

```

---

## 🔑 Default Credentials

For testing purposes:
- **PIN**: `1234`
- **Initial Balance**: `40,000`

> ⚠️ **Note**: These are hardcoded for educational purposes only. Production systems would use secure authentication mechanisms and database storage.

---

## 📂 Project Structure

```
.
├── atm.py              # Main ATM simulation program
├── main.py             # Text-to-speech integration
├── atm.ipynb           # Jupyter notebook with documentation
├── README.md           # Project documentation (this file)
└── LICENSE             # MIT License
```

---

## 🎯 Key Functionalities Explained

### PIN Verification
```python
pin = int(input('Enter your pin: '))
if pin == correct_pin:
    # Access granted - display menu
else:
    print('wrong pin')
```

### Withdrawal with Validation
```python
amount = int(input('enter the withdraw amount: '))
if amount <= balance:
    balance -= amount
    print('withdrawal successful')
else:
    print('insufficient balance')
```

### Deposit Processing
```python
amount = int(input('Enter deposit money: '))
balance += amount
print('Deposit successful')
```

---

## 🌱 Learning Outcomes

This project helps you practice:
- ✅ Conditional statements (`if/elif/else`)
- ✅ User input handling and validation
- ✅ Variable manipulation and arithmetic operations
- ✅ Program flow control
- ✅ Error handling basics
- ✅ Creating interactive console applications

---

## 🚧 Future Enhancements

- [ ] **Multiple User Accounts**: Support for multiple users with separate accounts
- [ ] **Transaction History**: Log and display recent transactions
- [ ] **Data Persistence**: Save account data to a file or database
- [ ] **Security Improvements**: 
  - PIN attempts limit with account lockout
  - Account password change functionality
  - Transaction PIN for withdrawals
- [ ] **Advanced Features**:
  - Interest calculation
  - Daily withdrawal limits
  - Account types (Savings/Checking)
  - Fund transfer between accounts
- [ ] **GUI Version**: Graphical user interface using tkinter or PyQt
- [ ] **API Integration**: Connect to a backend server

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🎓 Educational Resource

This project is designed as an educational tool for learning Python fundamentals. It's suitable for:
- Computer Science students
- Programming beginners
- Self-learners exploring Python
- Coding bootcamp participants

---

## 📞 Contact & Support

- **Author**: Dennis
- **Email**: your.email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

For issues, questions, or suggestions, please [open an issue](https://github.com/yourusername/python-atm-banking-system/issues) on GitHub.

---

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Best Practices](https://pep8.org/)
- [Banking System Design](https://en.wikipedia.org/wiki/Automated_teller_machine)

---

## 🎉 Acknowledgments

Thanks to everyone who has contributed ideas, feedback, and improvements to this project!

---

**Last Updated**: September 2026  
**Version**: 1.0.0

---

## 💡 Pro Tips

- Modify the PIN and initial balance in the code to test different scenarios
- Add print statements to debug transaction logic
- Expand the menu with additional banking operations
- Practice refactoring the code into functions for better organization

---

Happy Coding! 🚀
