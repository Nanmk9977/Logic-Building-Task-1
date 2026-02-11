stored_username = "admin"
stored_password = "1234"

print("Login System \n ")   # Taking input from the user
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Checking the credentials
if entered_username == stored_username and entered_password == stored_password:
    print("Login Successful")
else:
    print("Invalid Credentials")
