import getpass

print("=" * 40)
print("      Secure Login System")
print("=" * 40)

attempts = 3

while attempts > 0:
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    # Input Validation
    if username.strip() == "" or password.strip() == "":
        print("\nUsername and Password cannot be empty.")
        continue

    if username == "admin" and password == "123456":
        print("\nLogin Successful!")
        print("Welcome,", username)
        print("Access Granted")
        print("Loading Dashboard...")
        break

    else:
        attempts -= 1
        print("\nInvalid Username or Password!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\nAccount Locked!")
    print("Please try again later.")