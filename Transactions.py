from datetime import date
from Validation import validAmount, validCategory


# this will start the while loop for a user to input their transaction information
startProgram = (input("Do you want to enter a transaction?\n"))

while startProgram == "yes":

    # function to get user details
    def getTransactionDetails():

        # Required Information
        # This will return today's date for the user. This will allow us to track their spending
        today = date.today()

        transactionDate = today.strftime("Today is the %d/%m/%Y") # dd/mm/YY
        transactionAmount = validAmount()

        # Optional Information
        transactionDescription = input("Enter a description for the purchase e.g why you bought it: \n")

        return {
            "date": transactionDate,
            "amount": transactionAmount,
            "description": transactionDescription
        }


    def getTransactionCategory():

        print("From the list below, select a category for your transaction:")

        # Allow the user to choose a category for their transaction
        categories = ["Groceries", "Bills", "Pets", "Entertainment", "Car"]

        # loop through the categories list to show it to the user
        for i in categories:

            #display the categories
            print(i, end = "    ") # end = "" stops the print statement adding a new line after each iteration

        print("\n")

        category = validCategory(categories)

        return category


    # Lists all the transaction information
    transactions = (getTransactionDetails(), getTransactionCategory())
    print(transactions)

    break
