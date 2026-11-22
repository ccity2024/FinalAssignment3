#Dictionary of appliance names and kWh
appliances = {}

#Function displaying the main menu and accepting selection
def main_menu():
    print("Household Electricity Consumption Calculator")
    print("Press 1 to view electricity consumption")
    print("Press 2 to add household appliance")
    print("Press 3 to remove household appliance")
    print("Press 4 to quit program")

    selection = input("Selection: ")
    return selection

#Function to view all appliances
def view_electricity_consumption():
    #If appliances dictionary is empty go back to menu
    if not appliances:
        print("No appliances added yet.\n")
        return

    #Total kWh usage
    total = 0

    #Print all appliances in the appliances dictionary with its wattage, hours used, kWh
    for name, data in appliances.items():
        kwh = household_math(data["wattage"], data["hours"])
        total += kwh
        print(name + ": " + str(round(kwh, 2)) + " kWh")
    print("Total: " + str(round(total, 2)) + " kWh\n")

#Function to add household appliances in the appliances dictionary
def add_household_appliance():
    #Accept input of appliance name, wattage, and hours
    name = input("Enter name of appliance: ")

    wattage = float(input("Enter wattage of appliance: "))

    hours = float(input("Enter hours used per day: "))

    #Add appliance with the wattage and hours used in the appliance dictionary
    appliances[name] = {"wattage": wattage, "hours": hours}

    #Print success if the appliance was added and prints the kWh consumption
    print(name + " added. Consumption: " + str(household_math(wattage, hours)) + " kWh/day\n")

#Math to calculate the kWh of a appliance
def household_math(wattage, hours):
    #Formula is wattage * hours used divided by one thousand
    return (wattage * hours) / 1000

#Remove appliance from the appliances dictionary
def remove_household_appliance():
    #If appliances dictionary is empty go back to menu
    if not appliances:
        print("No appliances to remove.\n")
        return

    #Print all the appliances in the appliance dictionary
    print("Current appliances:")

    for i, name in enumerate(appliances, 1):
        #Print the number of the appliance and the name
        print(i, name)

    #Accept the name of the appliance that needs to be removed
    name = input("Enter name of appliance to remove: ")

    if name in appliances:
        #If the appliance is in the appliances dictionary then delete it
        del appliances[name]
        print(name + " removed.\n")
    else:
        #If the appliance is not in the appliances dictionary then print not found
        print(name + " not found.\n")

#Main menu loop
while True:
    user_selection = main_menu()

    if user_selection == "1":
        view_electricity_consumption()
    elif user_selection == "2":
        add_household_appliance()
    elif user_selection == "3":
        remove_household_appliance()
    elif user_selection == "4":
        print("Bye!")
        break
    else:
        #Go back to menu if input different number
        print("Invalid selection. Please try again.")



