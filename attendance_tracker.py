import csv
import os

students_file = "students.csv"
attendance_file = "attendance.csv"

students = {}  # roll -> {name, present, total}


# ----------------------------
# 1. Load existing data
# ----------------------------
def load_data():
    if os.path.exists(students_file):
        with open(students_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                roll, name, present, total = row
                students[roll] = {
                    "name": name,
                    "present": int(present),
                    "total": int(total)
                }


# ----------------------------
# 2. Save data
# ----------------------------
def save_data():
    with open(students_file, "w", newline="") as f:
        writer = csv.writer(f)
        for roll, data in students.items():
            writer.writerow([roll, data["name"], data["present"], data["total"]])


# ----------------------------
# 3. Add new student
# ----------------------------
def add_student(roll, name):
    if roll in students:
        print("⚠️ Student already exists!")
    else:
        students[roll] = {"name": name, "present": 0, "total": 0}
        print("✅ Student added successfully!")


# ----------------------------
# 4. Mark attendance
# ----------------------------
def mark_attendance(roll, status):
    if roll not in students:
        print("⚠️ Student not found!")
        return
    students[roll]["total"] += 1
    if status.upper() == "P":
        students[roll]["present"] += 1
    print("✅ Attendance marked.")


# ----------------------------
# 5. Calculate percentage
# ----------------------------
def calculate_percentage(roll):
    s = students[roll]
    if s["total"] == 0:
        return 0
    return (s["present"] / s["total"]) * 100


# ----------------------------
# 6. View report
# ----------------------------
def view_report():
    print("\n📋 Attendance Report")
    print("-" * 40)
    for roll, data in students.items():
        perc = calculate_percentage(roll)
        status = "⚠️ Low Attendance" if perc < 75 else "✅ Good"
        print(f"Roll: {roll}, Name: {data['name']}, Attendance: {perc:.2f}% {status}")


# ----------------------------
# Main Program
# ----------------------------
load_data()

while True:
    print("\n==== Student Attendance Tracker ====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Report")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        add_student(roll, name)
        save_data()

    elif choice == "2":
        roll = input("Enter Roll No: ")
        status = input("Present/Absent (P/A): ")
        mark_attendance(roll, status)
        save_data()

    elif choice == "3":
        view_report()

    elif choice == "4":
        save_data()
        print("💾 Data saved. Exiting...")
        break

    else:
        print("⚠️ Invalid choice! Try again.")
