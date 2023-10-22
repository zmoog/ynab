import io
from typing import List

from rich import box
from rich.console import Console
from rich.table import Table

from .models import AccountTransaction


class AccountTransactionsOutput:
    """Output a list of AccountTransaction objects in a table or a CSV file"""

    def __init__(self, transactions: List[AccountTransaction]):
        self.transactions = transactions

    def table(self) -> str:
        """Output a table with the transactions"""
        print(f"Found {len(self.transactions)} transactions")

        # Create a new table
        table = Table(
            title="Account transactions",
            # box=box.SIMPLE,
        )

        # Add columns
        table.add_column("Date")
        table.add_column("Amount")
        table.add_column("Description")
        table.add_column("Description full")
        table.add_column("State")
        table.add_column("MoneyMap category")

        # Add rows
        for transaction in self.transactions:
            table.add_row(
                str(transaction.date),
                str(transaction.amount),
                transaction.description,
                transaction.description_full,
                transaction.state,
                transaction.moneymap_category,
            )

        # turn table into a string using the Console
        console = Console(file=io.StringIO())
        console.print(table)

        return console.file.getvalue()

    def csv(self) -> str:
        """Output a CSV string with the transactions"""
        return "csv"
    