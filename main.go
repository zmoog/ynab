package main

import (
	"fmt"

	"github.com/extrame/xls"
)

type CreditCardTransaction struct {
	Owner            string
	CardNumber       string
	OperationDate    string
	RegistrationDate string
	Description      string
	OperationStatus  string
	OperationnType   string
	Circuit          string
	Type             string
	Amount           string
}

func main() {
	// Open the .xls file
	xlsFile, err := xls.Open("2023-06 mastercard.xls", "utf-8")
	// xlsFile, err := xls.Open("2023-04 Fineco.xls", "utf-8")
	// xlsFile, err := xls.Open("estrattoconto(13).xls", "utf-8")
	if err != nil {
		fmt.Printf("Error opening file: %s\n", err)
		return
	}

	// Read the sheets in the .xls file
	sheet := xlsFile.GetSheet(0) // Assuming the first sheet is the one you want to read
	if sheet == nil {
		fmt.Println("Sheet not found")
		return
	}

	// Iterate over rows in the sheet
	for i := 0; i <= int(sheet.MaxRow); i++ {
		row := sheet.Row(i)

		lastCol := row.LastCol() // Find the last column in the row
		// fmt.Printf("%d\t", lastCol)

		// We expect data rows to have 11 columns.
		if lastCol != 11 {
			continue
		}

		// We assume that the first column is the owner of the credit card.
		// If the owner column is empty, we skip the row.
		owner := row.Col(1)
		if owner == "" {
			continue
		}

		transaction := CreditCardTransaction{
			Owner:            owner,
			CardNumber:       row.Col(2),
			OperationDate:    row.Col(3),
			RegistrationDate: row.Col(4),
			Description:      row.Col(5),
			OperationStatus:  row.Col(6),
			OperationnType:   row.Col(7),
			Circuit:          row.Col(8),
			Type:             row.Col(9),
			Amount:           row.Col(10),
		}

		fmt.Printf("%+v\n", transaction)
	}
}
