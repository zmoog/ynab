import click
import xlrd


@click.group()
@click.version_option()
def cli():
    "CLI tool to support data import and export from YNAB"


@cli.group()
def fineco():
    "Fineco related commands"

@fineco.command(name="read-credit-card")
@click.argument(
    "excel-file",
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def read_credit_card(excel_file, option):
    "Read a credit card statement and output a table or a CSV file"
    click.echo("Here is some output")

    # Open the workbook
    workbook = xlrd.open_workbook(excel_file)

    # Select the first sheet (index 0) from the workbook
    sheet = workbook.sheet_by_index(0)

    # Read data from cells
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            cell_value = sheet.cell_value(row, col)
            print(cell_value)