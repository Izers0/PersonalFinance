from datetime import date
from Validation import validAmount, validCategory


# function to get user details
def getTransactionDetails():

    # Required Information
    # This will return today's date for the user. This will allow us to track their spending
    today = date.today()

    transactionDate = today.strftime("%d/%m/%Y") # dd/mm/YY

    # put the function for the validAmount into a variable
    transactionAmount = validAmount()

    # Optional Information
    transactionDescription = input("Enter a description for the purchase e.g why you bought it: \n")

    # return all the information given by the user
    return {
        "date": transactionDate,
        "amount": transactionAmount,
        "description": transactionDescription
    }


# function to get the category of the users transaction
def getTransactionCategory():

    print("From the list below, select a category for your transaction:")

    # Allow the user to choose a category for their transaction
    categories = ["Groceries", "Bills", "Pets", "Entertainment", "Car"]

    # loop through the categories list to show it to the user
    for i in categories:

        #display the categories
        print(i, end = "    ") # end = "" stops the print statement adding a new line after each iteration

    print("\n")

    # put the function for the validCategories into a variable
    category = validCategory(categories)

    # return the user inputs to the console
    return category

# this will start the while loop for a user to input their transaction information
startProgram = (input("Do you want to enter a transaction?\n")).strip().lower()

while startProgram == "yes":
    # Lists all the transaction information
    transactions = (getTransactionDetails(), getTransactionCategory())

    # print all transaction details
    print("Transaction Details:")
    print(f"Date: {transactions[0]['date']}")  # [0] is for the index of the function from the transactions variable
    print(f"Amount: £{transactions[0]['amount']}")
    print(f"Description: {transactions[0]['description']}")
    print(f"Category: {transactions[1]}")

    # ask the user if they want to add another transaction to restart the program
    startProgram = (input("Do you want to enter a transaction?\n")).strip().lower()

# message to show the program has ended
print("Goodbye")

#testing git