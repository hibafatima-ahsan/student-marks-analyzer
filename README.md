# Student Marks Analyzer using NumPy

A simple menu-driven Python application built with **NumPy** that loads student marks from a CSV file and performs various data analysis tasks.

---

## Features

- Load student marks from a CSV dataset
- Display dataset summary
- View complete student dataset
- Calculate overall statistics
  - Average marks
  - Highest marks
  - Lowest marks
  - Standard deviation
- Calculate subject-wise averages
- Find the top-performing student
- Display students with an average of 80 or above
- Add bonus marks to all students using NumPy
- Menu-driven Command Line Interface (CLI)

---

## Technologies Used

- Python 3
- NumPy

---

## Project Structure

```
Student_Marks_Analyzer/
│
├── main.py
├── student_marks.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

The project uses a CSV file containing:

| Column | Description |
|--------|-------------|
| Student | Student Name |
| Math | Math Marks |
| Science | Science Marks |
| English | English Marks |

Example:

```csv
Student,Math,Science,English
Ali,78,85,90
Sara,92,88,95
Ahmed,65,70,68
...
```

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/hibafatima-ahsan/student-marks-analyzer
```

### Navigate to the project

```bash
cd Student_Marks_Analyzer
```

### Install NumPy

```bash
pip install numpy
```

### Run the project

```bash
python main.py
```

---

## Menu

```
Student Marks Analyzer

1. Dataset Summary
2. Display Dataset
3. Student Analysis
4. Subject-wise Average
5. Top Performer
6. Students Above 80
7. Add Bonus Marks
8. Exit
```

---

## Learning Outcomes

This project demonstrates:

- Loading CSV files using NumPy
- Working with structured arrays
- Array indexing and slicing
- Statistical functions (`mean`, `max`, `min`, `std`)
- Boolean indexing
- Array operations
- Modular programming using functions
- Building a menu-driven CLI application

---

## Author

**Ayela Ahsan**
**Hiba Fatima**
