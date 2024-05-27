def to_upper_case(string):
    return string.upper()

def to_lower_case(string):
    return string.lower()

def reverse_string(string):
    return string[::-1]

while True:
    print("Choose an option:")
    print("1. Convert string to upper case")
    print("2. Convert string to lower case")
    print("3. Reverse the string")
    
    choice = input("Enter your choice: ")
    
    if choice not in {'1', '2', '3'}:
        print("Invalid choice.")
        continue
    
    user_string = input("Enter the string: ")
    
    if choice == '1':
        result = to_lower_case(user_string)
    elif choice == '2':
        result = to_upper_case(user_string)
    elif choice == '3':
        result = reverse_string(user_string)
    
    print(f"Result: {result}")
    
    continue_process= input("Do you want to continue? (y/n): ").strip().lower()
    if continue_process!= 'y':
        break
