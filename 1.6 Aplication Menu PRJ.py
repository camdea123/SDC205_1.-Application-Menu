from datetime import datetime

print("CAMDEA1617 - Spreadsheet Automation Menu")

print("\n\n1. Input Data\n2. View Current Data\n3. Generate Report\n")

#The next line retrieves the inputted option and stores into the variable called <input>
choice = input()

selection_time = datetime.now()

print ("You selected",choice,f"on: {selection_time}")
