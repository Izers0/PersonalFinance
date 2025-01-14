from datetime import date

# validation of transactionAmount
def validAmount(amount):
    return amount > 0

# this will start the while loop for a user to input their transaction information
startProgram = (input("Do you want to enter a transaction?\n"))

while startProgram == "yes":

    # Required Information
    # This will return today's date for the user. This will allow us to track their spending
    today = date.today()

    transactionDate = today.strftime("Today is the %d/%m/%Y") # dd/mm/YY
    transactionAmount = int(input("How much did you spend: £"))


    # Allow the user to choose a category for their transaction
    categories = ["Groceries", "Bills", "Pets", "Entertainment", "Car"]
    print("Enter a category for your transaction from the list:\n")

    # loop through the categories list to show it to the user
    for i in categories:
        #display the categories
        print(i, end = "    ") # end = "" stops the print statement adding a new line after each iteration

    # allow a choice from the user
    transactionCategory = input("\n").strip().lower()

# need to fix case sensitivity

    if transactionCategory == "Groceries":
        print("\n")
    elif transactionCategory == "Bills":
        print("\n")
    elif transactionCategory == "Pets":
        print("\n")
    elif transactionCategory == "Entertainment":
        print("\n")
    elif transactionCategory == "Car":
        print("\n")
    else:
        print("Not a valid category")

    # Optional Information
    transactionDescription = input("Enter a description for the purchase e.g why you bought it: \n")


    # Lists all the transaction information
    transactions = (transactionDate, transactionAmount, transactionCategory, transactionDescription)


    # check to see the transactionAmount is above 0
    if validAmount(transactionAmount):
        for i in transactions:
            print(i)

        print(f"You spent £{transactionAmount}. This has been added to the tracker")

    else:
        print("This is an invalid value. Please enter a positive amount")
