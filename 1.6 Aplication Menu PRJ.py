from datetime import datetime

print("CAMDEA1617 - Spreadsheet Automation Menu")

menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report",
]

for option in menu_options:
    print(option)

choice = input("Enter your choice: ")
selection_time = datetime.now()

if choice in ["1", "2", "3",]:
    print (f"You selected {choice} on: {selection_time}")
else:
    print("Error: Invalid choice selected.")


