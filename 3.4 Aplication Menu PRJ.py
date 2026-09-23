from datetime import datetime

print("CAMDEA1617 - Spreadsheet Automation Menu")

def convertData(temp):
    return (temp -32)*5/9
    

def getInput():
    
    entries = int(input("How many entries are you inputting? "))

    for i in range(entries):
        date = input("Enter a date: ")
        temp = int(input("Enter the highest temp for the selected date: "))

        tempInCelcius = convertData(temp)

        print(f"\nThe following was saved at {datetime.now()}:")
        print(f"Date: {date}\nOriginal Temp: {temp}\nConverted Temp: {tempInCelcius:.2f}\n\n")
    
        

        
    

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
    
if choice == "1":
    getInput()
    
else:
    print("Error: The chosen functionality is not implemented yet")


