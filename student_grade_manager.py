students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records found.")
        else:
            print("\nStudent Records")
            for name, marks in students.items():
                if marks >= 90:
                    grade = "A"
                elif marks >= 75:
                    grade = "B"
                elif marks >= 50:
                    grade = "C"
