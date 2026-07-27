import numpy as np


# Load Dataset
def load_dataset():
    try:
        data = np.genfromtxt(
            "student_marks.csv",
            delimiter=",",
            names=True,
            dtype=None,
            encoding="utf-8"
        )
        print("\nDataset loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: student_marks.csv not found.")
        return None


# Dataset Summary
def dataset_summary(data):

    print("\nDataset Summary")
    print("-" * 30)

    print("Rows:", data.shape[0])
    print("Columns:", len(data.dtype.names))
    print("Column Names:", data.dtype.names)
    print("Shape:", data.shape)
    print("Size:", data.size)
    print("Dimensions:", data.ndim)


# Display Dataset
def display_dataset(data):

    print("\nStudent Dataset")
    print("-" * 30)

    for row in data:
        print(row)


# Student Analysis
def student_analysis(data):

    marks = np.column_stack((
        data["Math"],
        data["Science"],
        data["English"]
    ))

    print("\nStudent Analysis")
    print("-" * 30)

    print("Average Marks:", np.mean(marks))
    print("Highest Marks:", np.max(marks))
    print("Lowest Marks:", np.min(marks))
    print("Standard Deviation:", np.std(marks))


# Subject-wise Average
def subject_average(data):

    print("\nSubject-wise Average")
    print("-" * 30)

    print("Math:", np.mean(data["Math"]))
    print("Science:", np.mean(data["Science"]))
    print("English:", np.mean(data["English"]))


# Top Performer
def top_student(data):

    total = data["Math"] + data["Science"] + data["English"]

    index = np.argmax(total)

    print("\nTop Performer")
    print("-" * 30)

    print("Student:", data["Student"][index])
    print("Total Marks:", total[index])


# Students Above 80 Average
def students_above_80(data):

    average = (
        data["Math"] +
        data["Science"] +
        data["English"]
    ) / 3

    students = data[average >= 80]

    print("\nStudents with Average >= 80")
    print("-" * 30)

    if len(students) == 0:
        print("No student found.")
    else:
        for student in students:
            print(student["Student"])


# Add Bonus Marks
def bonus_marks(data):

    print("\nMarks After Adding 5 Bonus Marks")
    print("-" * 30)

    updated = np.column_stack((
        data["Math"] + 5,
        data["Science"] + 5,
        data["English"] + 5
    ))

    print(updated)


# Main Function
def main():

    data = load_dataset()

    if data is None:
        return

    while True:

        print("\nStudent Marks Analyzer")
        print("1. Dataset Summary")
        print("2. Display Dataset")
        print("3. Student Analysis")
        print("4. Subject-wise Average")
        print("5. Top Performer")
        print("6. Students Above 80")
        print("7. Add Bonus Marks")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            dataset_summary(data)

        elif choice == "2":
            display_dataset(data)

        elif choice == "3":
            student_analysis(data)

        elif choice == "4":
            subject_average(data)

        elif choice == "5":
            top_student(data)

        elif choice == "6":
            students_above_80(data)

        elif choice == "7":
            bonus_marks(data)

        elif choice == "8":
            print("\nThank you for using Student Marks Analyzer!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()