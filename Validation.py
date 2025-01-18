# validation of transactionAmount
def validAmount():

    while True:
        try:
            amount = float(input("How much did you spend: £"))

            if amount > 0:
                return amount

            else :
                print("Invalid Input. Please Enter a number that is positive")

        except ValueError:
            print("Please enter a valid number")


# Ensure category is chosen from the list
def validCategory(categories):

    while True:
        # Allow a choice from the user
        try:

            print("Enter a category for your transaction from the list:\n")

            userInput = input("")
            transactionCategory = userInput.lower()

            # Normalize the categories list to lowercase for comparison
            if transactionCategory in [category.lower() for category in categories]:
                print("\nCategory selected:", userInput.capitalize())

                return transactionCategory

        except ValueError:
            print("Please Enter a Category from the List")
