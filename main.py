#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the main test file for the ABM-Ldgr.py toolkit.
Basically, this includes example code that exercises
most of the core functionality of the toolkit.

Copyright 2022-Present Don Berndt @ University of South Florida.

@author: Don Berndt (dberndt@usf.edu)
"""

# Import needed resources.
from ldgr import *

print("\nInstantiating accounts ...")
# Create an initial account with a starting balance of zero.
# This will serve as a cash account on the balance sheet.
# A couple of tags are added for use in searches.
cash_account = Account("Cash",
                       0,
                       {'asset', 'cash', 'liquid'},
                       "Current cash.",
                       "green")

# Look at the account information.
cash_account.show()

# Print the current balance.
print("Cash Balance:", cash_account.balance())

# Make a deposit and withdrawal.
cash_account.deposit(1000)
cash_account.withdraw(100)
print("New Cash Balance:", cash_account.balance())

# Create second account for pending invoices with
# an initial balance of 100,000.
invoice_account = Account("Invoices",
                          100000,
                          {'asset', 'invoices'},
                          "Pending invoices.",
                          "blue")
invoice_account.show()

print("\nInstantiating ledgers ...")
# Group the cash and invoices into an list of assets.
assets_list = [cash_account, invoice_account]

assets_ledger = Ledger("Assets", assets_list)
assets_ledger.show()
assets_ledger.pprint()

# Creat a liabilities ledger with a loans account.
liabilities_ledger = Ledger("Liabilities",
                            [Account("Loans",
                                     30000,
                                     {'liability', 'loans'},
                                     "Outstanding loans.",
                                     "red")])
liabilities_ledger.pprint()

print("\nInstantiating balance sheet ...")
# Create a balance sheet based on the assets and liabilities ledgers.
balance_sheet = BalanceSheet("Balance Sheet",
                             assets_ledger,
                             liabilities_ledger)
balance_sheet.pprint()

print("\nCapturing snapshots ...")
# Handle cash deposits and withdrawals using snapshots.
# Snapshots are useful for capturing daily balances or
# any periodic changes to create a data series.
cash_account.withdraw(100)
cash_account.snapshot()
cash_account.withdraw(100)
cash_account.snapshot()
cash_account.deposit(300)
cash_account.snapshot()
print("Snapshots:", cash_account.snapshots())

print("\nBalance sheet ...")
balance_sheet.pprint()
