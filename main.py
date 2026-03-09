from functions import *

while True:

    print("\n===== Student Performance System =====")

    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Save Data")
    print("6. Load Data")
    print("7. Statistics")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        find_topper()

    elif choice == "5":
        save_data()

    elif choice == "6":
        load_data()

    elif choice == "7":
        subject_average()
        standard_deviation()
        grade_distribution()

    elif choice == "8":
        print("Program ended")
        break

    else:
        print("Invalid choice")