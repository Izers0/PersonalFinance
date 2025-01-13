# User login

# Makes the file which will store the usernames
files = "Usernames.txt"


# function to save usernames to the Usernames.txt file
def save(input, filename):

    # with open is used so we don't have to close the file every time
    with open(filename, "w") as file:
        file.write(input)


def load(filename):

    with open(filename, "r") as file:
        read = file.read()
    return read
