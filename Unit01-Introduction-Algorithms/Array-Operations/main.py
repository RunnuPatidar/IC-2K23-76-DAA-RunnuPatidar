# Python implementation of Array-Operations

# Experiment 1: Basic Operations on Arrays

def display_array(arr):
    print("Current Array:", arr)


def insert_element(arr):
    try:
        element = int(input("Enter element to insert: "))
        position = int(input("Enter position (0-based): "))

        if position < 0 or position > len(arr):
            print("Invalid position!")
            return

        arr.insert(position, element)
        print("Element inserted successfully.")

    except ValueError:
        print("Please enter valid integers.")


def delete_element(arr):
    try:
        position = int(input("Enter position to delete: "))

        if position < 0 or position >= len(arr):
            print("Invalid position!")
            return

        removed = arr.pop(position)
        print("Deleted element:", removed)

    except ValueError:
        print("Please enter a valid position.")


def search_element(arr):
    try:
        element = int(input("Enter element to search: "))

        if element in arr:
            print("Element found at index:", arr.index(element))
        else:
            print("Element not found.")

    except ValueError:
        print("Please enter a valid integer.")


def main():
    arr = [10, 20, 30, 40, 50]

    while True:
        print("\n--- ARRAY OPERATIONS ---")
        print("1. Display Array")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Search Element")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_array(arr)

        elif choice == '2':
            insert_element(arr)

        elif choice == '3':
            delete_element(arr)

        elif choice == '4':
            search_element(arr)

        elif choice == '5':
            print("Program terminated.")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
