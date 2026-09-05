from datetime import datetime

print("CAMDEA1617 - Spreadsheet Automation Menu")

print("\n\n1. Input Data\n2. View Current Data\n3. Generate Report\n")

choice = input()
selection_time = datetime.now()

print ("You selected",choice,f"on: {selection_time}")
