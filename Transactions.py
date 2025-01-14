from datetime import date

# validation of transactionAmount
def validAmount(amount):
    return amount > 0


# Required Information
# This will return today's date for the user. This will allow us to track their spending
today = date.today()

transactionDate = today.strftime("Today is the %d/%m/%Y") # dd/mm/YY
transactionAmount = int(input("How much did you spend: £"))
transactionCategory = input("What type of transaction was this: ") # later make this a menu

# Optional Information
transactionDescription = input("Enter a description for the purchase e.g why you bought it: ")


# Lists all the transaction information
transactions = (transactionDate, transactionAmount, transactionCategory, transactionDescription)


# check to see the transactionAmount is above 0
if validAmount(transactionAmount):
    for i in transactions:
        print(i)

    print(f"You spent £{transactionAmount}. This has been added to the tracker")

else:
    print("This is an invalid value. Please enter a positive amount")
