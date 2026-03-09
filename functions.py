from student import Student

students = []

def add_student():

    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    marks = []

    subjects = [
        "Mathematics",
        "Physics",
        "Programming",
        "Electronics",
        "Signal Processing"
    ]

    for sub in subjects:
        m = int(input(f"Enter marks for {sub}: "))
        marks.append(m)

    s = Student(sid, name, branch, marks)
    students.append(s)

    print("Student added successfully")


def display_students():

    for s in students:

        print("------------------------")
        print("ID:", s.student_id)
        print("Name:", s.name)
        print("Branch:", s.branch)
        print("Marks:", s.marks)
        print("Total:", s.calculate_total())
        print("Average:", s.calculate_average())
        print("Grade:", s.calculate_grade())


def search_student():

    sid = input("Enter ID to search: ")

    for s in students:

        if s.student_id == sid:
            print("Student Found")
            print("Name:", s.name)
            print("Branch:", s.branch)
            print("Marks:", s.marks)
            return

    print("Student not found")


def find_topper():

    if len(students) == 0:
        print("No student data")
        return

    topper = students[0]

    for s in students:

        if s.calculate_total() > topper.calculate_total():
            topper = s

    print("Topper:", topper.name)
    print("Total:", topper.calculate_total())


def save_data():

    file = open("students.txt", "w")

    for s in students:

        line = s.student_id + "," + s.name + "," + s.branch

        for m in s.marks:
            line += "," + str(m)

        file.write(line + "\n")

    file.close()

    print("Data saved to file")


def load_data():

    try:
        file = open("students.txt", "r")

        for line in file:

            data = line.strip().split(",")

            sid = data[0]
            name = data[1]
            branch = data[2]

            marks = list(map(int, data[3:]))

            s = Student(sid, name, branch, marks)
            students.append(s)

        file.close()

        print("Data loaded successfully")

    except:
        print("File not found")

def subject_average():

    if len(students) == 0:
        print("No student data")
        return

    subjects = ["Mathematics","Physics","Programming","Electronics","Signal Processing"]

    totals = [0,0,0,0,0]

    for s in students:
        for i in range(5):
            totals[i] += s.marks[i]

    print("\nAverage Marks Per Subject")

    for i in range(5):
        avg = totals[i] / len(students)
        print(subjects[i], "Average:", round(avg,2))

def standard_deviation():

    if len(students) == 0:
        print("No student data")
        return

    averages = []

    for s in students:
        averages.append(s.calculate_average())

    mean = sum(averages) / len(averages)

    variance = 0

    for a in averages:
        variance += (a - mean) ** 2

    variance = variance / len(averages)

    std = variance ** 0.5

    print("Standard Deviation:", round(std,2))

def grade_distribution():

    grades = {"A":0,"B":0,"C":0,"D":0,"F":0}

    for s in students:
        g = s.calculate_grade()
        grades[g] += 1

    print("\nGrade Distribution")

    for g in grades:
        print(g, ":", grades[g])