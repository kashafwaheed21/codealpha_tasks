print("=" * 40)
print("      Login System")
print("=" * 40)

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "123456":
    print("\nLogin Successful!")
    print("Access Granted")
    print("Loading Dashboard...")
    print("Welcome,", username)
else:
    print("\nInvalid Username or Password!")