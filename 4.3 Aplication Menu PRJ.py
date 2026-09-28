import csv
from datetime import datetime

print("CAMDEA1617 - Spreadsheet Automation Menu")

#Inserts comma-seperated data into a CSV file.

def insertData(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data + "\n")
    except Exception as error:
        print("Error writin to file:", error)
        
#Displays contents of a CSV file
def viewData(file_path):
    try:
        with open(file_path, "r") as file:
            print ("\nFile:", file_path)
            for line in file:
                print(line.strip())
    except Exception as error:
        print("Error reading file:", error)
 #Converts temp in farenheit to celcius       

def convertData(temp):
    return (temp -32)*5/9
    
#Takes entires for temp during specified dates, converts them to celcius, then creates a CSV describing the date chosen
#and both temps before formatting that data into comma-seperated data and then saving it to the CSV file
def getInput():
    
    entries = int(input("How many entries are you inputting? "))

    for i in range(entries):
        date = input("Enter a date: ")
        temp = int(input("Enter the highest temp for the selected date: "))
        
        #Takes the entered temp from the previous input and converts it using our convertData function
        #the name is convertData, the argument is the temp the user inputted and the return value is the
        #temperature after being converted to Celcious using the conversion formula
        tempInCelcius = convertData(temp)

        #Creates comma seperated data for the entrie
        data = f"{date},{temp},{tempInCelcius:.2f}"

        #Writes to file
        insertData("ZooData.csv", data)

        print(f"\nThe following was saved at {datetime.now()}: {data}.")

    
        

        
    

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
elif choice == "2":
    viewData("ZooData.csv")
    
else:
    print("Error: The chosen functionality is not implemented yet")


