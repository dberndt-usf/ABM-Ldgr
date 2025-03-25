#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This package defines the Account, Ledger,
and  BalanceSheet classes for use financial in agent-based models.
A ledger is a collection of accounts that are associated
with specific agents forming balance sheets.

Copyright 2022-Present Don Berndt @ University of South Florida.

@author: Don Berndt (dberndt@usf.edu)
"""

# Import needed resources.
import matplotlib.pyplot as plt
from tabulate import tabulate

################################################################
# This is the core Ledger class for the ledger.py package
# that implements a collection financial accounts for an agent.
# Some accounts are shared among different agents,
# appearing on multiple balance sheets,
# thereby creating pathways for agent interactions.
class Ledger:
    # Declare class-specific variables.
    led_kind = 'LED'
    led_title = 'Ledger'
    debug = 0

    # Initialize account.
    def __init__(self, name, accounts):
        # Initialize the core class data.
        self.led_name = str(name)
        self.led_accounts = accounts

    def accounts(self):
        return self.led_accounts

    def total(self):
        total = float(0)
        for acc in self.led_accounts:
            total += acc.balance()
        return total

    def show(self):
        print(self.led_name)
        for acc in self.led_accounts:
            print(acc.name(), acc.balance())

    def pprint(self, show_currency=False):
        print(self.led_name)
        if bool(self.led_accounts):
            table = []
            # Check for zero total ledger balance to
            # avoid divide by zero errors.
            if self.total() > 0:
                for acc in self.led_accounts:
                    if show_currency:
                        acc_name = acc.name() + " (" + acc.code() + ")"
                    else:
                        acc_name = acc.name()
                    table.append([acc_name,
                                  acc.balance(),
                                  (acc.balance() / self.total()) * 100])
                if show_currency:
                    # Get currency symbol from first account.
                    title = "Balance (" + self.led_accounts[0].symbol() + ")"
                else:
                    title = "Balance"
                print(tabulate(table,
                               headers=["Account",
                                        title,
                                        "Percentage (%)"],
                               tablefmt="simple",
                               numalign="right",
                               floatfmt=",.2f"))
            else:
                for acc in self.led_accounts:
                    table.append([acc.name(),
                                  acc.balance()])
                print(tabulate(table,
                               headers=["Account",
                                        "Balance (" + self.led_accounts[0].symbol() + ")"],
                               tablefmt="simple",
                               numalign="right",
                               floatfmt=",.2f"))
        else:
            print("NA")  # Empty list.



################################################################
# This is the account class for the ledger.py package.
# Some accounts are shared among different agents,
# appearing on multiple balance sheets (or ledgers),
# thereby creating pathways for agent interactions.
class Account:
    # Declare class-specific variables.
    acc_kind = 'ACC'
    acc_title = 'Account'
    debug = 0

    # Initialize account.
    def __init__(self, name, balance, tag, note, color):
        # Initialize the core class data.
        self.acc_name = str(name)
        self.acc_balance = float(balance)
        self.acc_tag = str(tag)
        self.acc_note = str(note)
        self.acc_deposits = []
        self.acc_withdrawals = []
        self.acc_snapshots = [self.acc_balance]
        self.currency_code = 'USD'
        self.currency_symbol = '\u0024'
        self.currency_ppf = '\u0024{:,.2f}'  # Pretty print format
        self.viz_color = str(color)

    def name(self):
        return self.acc_name

    def symbol(self, curr_symbol=None):
        if curr_symbol is not None:
            # Update currency symbol.
            self.currency_symbol = curr_symbol
        return self.currency_symbol

    def code(self, curr_code=None):
        if curr_code is not None:
            # Update currency code.
            self.currency_code = curr_code
        return self.currency_code

    def color(self):
        return self.viz_color

    def withdraw(self, amount):
        self.acc_balance -= amount
        self.acc_withdrawals.append(amount)

    def withdrawals(self):
        return self.acc_withdrawals

    def deposit(self, amount):
        self.acc_balance += amount
        self.acc_deposits.append(amount)

    def deposits(self):
        return self.acc_deposits

    def balance(self):
        return self.acc_balance

    def snapshot(self):
        self.acc_snapshots.append(self.acc_balance)

    def snapshots(self):
        return self.acc_snapshots

    def show(self):
        print(self.acc_kind, self.acc_name, self.acc_tag, self.acc_balance)
        print(self.acc_note)

    def tag(self):
        return self.acc_tag



################################################################
# This is the balance sheet class for the ledger.py package
# used to implement a specialized structure that combines ledgers
# representing both the assets and liabilities of an agent.
class BalanceSheet:
    # Declare class-specific variables.
    bal_kind = 'BAL'
    bal_title = 'Balance Sheet'
    debug = 0

    # Initialize account.
    def __init__(self, name, assets, liabilities):
        # Initialize the core class data.
        self.bal_name = str(name)
        self.bal_assets = assets
        self.bal_liabilities = liabilities

    def name(self):
        return self.bal_name

    def assets(self):
        return self.bal_assets

    def liabilities(self):
        return self.bal_liabilities

    def show(self):
        print(self.bal_kind, self.name)

    def pprint(self, show_currency=False):
        print(self.bal_name)
        self.bal_assets.pprint(show_currency)
        self.bal_liabilities.pprint(show_currency)

    def plot(self, ticks, y_max):
        # Fix x-axis and y-axis ranges.
        x_min = 0
        x_max = max(ticks - 1, 10)
        y_min = 0.0
        # Configure the plot.
        plt.figure()
        ax = plt.subplot()
        # Get the data series (assets and liabilities).
        for acc in self.bal_assets.accounts():
            ax.plot(acc.snapshots(), color=acc.color())
        for acc in self.bal_liabilities.accounts():
            ax.plot(acc.snapshots(), color=acc.color())
        # Assemble legend.
        legend = []
        for acc in self.bal_assets.accounts():
            legend.append(acc.name())
        for acc in self.bal_liabilities.accounts():
            legend.append(acc.name())
        ax.legend(legend)
        ax.set_title(self.bal_name)
        plt.xlabel('Simulation Ticks')
        plt.ylabel('Balances')
        plt.axis([x_min, x_max, y_min, y_max])
        plt.show()
