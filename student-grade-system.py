def student_grade_system():
    print("Welcome to the Student Grade System!")

    students = {}

    while True:
        print("\nChoose an option:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. View Students")
        print("4. Quit")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            name = input("Enter student name: ")
            score = input("Enter student score: ")
            students[name] = score
            print(f"{name} added with score {score}.")

        elif option == "2":
            name = input("Enter student name to remove: ")
            if name in students:
                del students[name]
                print(f"{name} has been removed.")
            else:
                print("Student not found!")

        elif option == "3":
            if not students:
                print("No students in the system.")
            else:
                print("\nStudents and their Scores:")
                for name, score in students.items():
                    print(f"{name}: {score}")

        elif option == "4":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


# run program
student_grade_system()
