def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()  # This will work because display_menu is already defined
        choice = input("Enter your choice: ")
        # rest of your code...

if __name__ == "__main__":
    main()

