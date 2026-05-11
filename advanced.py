# Student Grades Visualizer
# Advanced Version

# Import matplotlib
import matplotlib.pyplot as plt


# -----------------------------------
# STUDENT DATA
# -----------------------------------

students = {

    "Ram": {
        "Math": 85,
        "Science": 78,
        "English": 90
    },

    "Sita": {
        "Math": 95,
        "Science": 88,
        "English": 92
    },

    "Hari": {
        "Math": 60,
        "Science": 72,
        "English": 68
    },

    "Gita": {
        "Math": 80,
        "Science": 85,
        "English": 84
    }

}


# -----------------------------------
# STUDENT REPORT
# -----------------------------------

percentages = {}

print("STUDENT REPORT")
print("-----------------------------------")

for student in students:

    print("\nStudent Name:", student)

    total = 0
    subject_count = 0

    # Subject loop
    for subject in students[student]:

        marks = students[student][subject]

        print(subject, ":", marks)

        total = total + marks
        subject_count = subject_count + 1

    # Percentage calculation
    percentage = total / subject_count

    percentages[student] = percentage

    print("Total Marks:", total)
    print("Percentage:", percentage)


# -----------------------------------
# OVERALL TOPPER
# -----------------------------------

topper = max(percentages, key=percentages.get)

print("\n-----------------------------------")
print("OVERALL TOPPER")
print("-----------------------------------")

print(topper, "with", percentages[topper], "%")


# -----------------------------------
# LOWEST STUDENT
# -----------------------------------

lowest_student = min(percentages, key=percentages.get)

print("\nLOWEST STUDENT")

print(lowest_student, "with", percentages[lowest_student], "%")


# -----------------------------------
# SUBJECT-WISE TOPPER
# -----------------------------------

subjects = ["Math", "Science", "English"]

print("\n-----------------------------------")
print("SUBJECT TOPPERS")
print("-----------------------------------")

for subject in subjects:

    highest_marks = -1
    topper_name = ""

    for student in students:

        marks = students[student][subject]

        if marks > highest_marks:

            highest_marks = marks
            topper_name = student

    print(subject, "Topper:", topper_name, "-", highest_marks)


# -----------------------------------
# SUBJECT-WISE LOWEST
# -----------------------------------

print("\n-----------------------------------")
print("SUBJECT LOWEST")
print("-----------------------------------")

for subject in subjects:

    lowest_marks = 999
    lowest_name = ""

    for student in students:

        marks = students[student][subject]

        if marks < lowest_marks:

            lowest_marks = marks
            lowest_name = student

    print(subject, "Lowest:", lowest_name, "-", lowest_marks)


# -----------------------------------
# OVERALL PERCENTAGE CHART
# -----------------------------------

student_names = []
student_percentages = []

for student in percentages:

    student_names.append(student)

    student_percentages.append(percentages[student])


# Create percentage chart
bars = plt.bar(student_names, student_percentages)

# Add marks above bars
for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(round(height, 2)),
        ha="center"
    )

# Labels
plt.title("Overall Percentage Chart")
plt.xlabel("Students")
plt.ylabel("Percentage")

# Show chart
plt.show()


# -----------------------------------
# SUBJECT-WISE VISUALIZATION
# -----------------------------------

for subject in subjects:

    student_names = []
    subject_marks = []

    # Collect subject data
    for student in students:

        student_names.append(student)

        marks = students[student][subject]

        subject_marks.append(marks)

    # Create chart
    bars = plt.bar(student_names, subject_marks)

    # Add marks above bars
    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            str(height),
            ha="center"
        )

    # Labels
    plt.title(subject + " Marks Chart")
    plt.xlabel("Students")
    plt.ylabel("Marks")

    # Show graph
    plt.show()
