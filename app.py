students = {}

while True:
    print("\n1. Add Student")
    print("2. View Results")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        python = int(input("Python marks: "))
        java = int(input("Java marks: "))
        sql = int(input("SQL marks: "))

        total = python + java + sql
        average = total / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "D"

        students[name] = {
            "total": total,
            "average": average,
            "grade": grade
        }

        print("Student added successfully")

    elif choice == 2:
        for name, result in students.items():
            print(
                name,
                result["total"],
                result["average"],
                result["grade"]
            )

    elif choice == 3:
        name = input("Enter student name: ")

        if name in students:
            print(students[name])
        else:
            print("Student not found")

    elif choice == 4:
        break

    else:
        print("Invalid choice")