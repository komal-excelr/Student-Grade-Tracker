Name: Komal Warpe
Topic: student Grade Tracker


import tkinter as tk
from tkinter import messagebox

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to calculate letter grade and GPA based on average grade
def calculate_letter_grade_and_gpa(average_grade):
    if average_grade >= 90:
        return 'A+', 4.0
    elif 80 <= average_grade < 90:
        return 'A', 3.7
    elif 70 <= average_grade < 80:
        return 'B+', 3.3
    elif 60 <= average_grade < 70:
        return 'B', 3.0
    elif 50 <= average_grade < 60:
        return 'C+', 2.7
    elif 40 <= average_grade < 50:
        return 'C', 2.0
    else:
        return 'F', 0.0

# Function to process the grades
def process_grades():
    try:
        # Get grades from input fields
        grades = [
            float(entry_english.get()),
            float(entry_hindi.get()),
            float(entry_marathi.get()),
            float(entry_maths.get()),
            float(entry_science.get())
        ]

        # Validate that all grades are within the correct range (0-100)
        for grade in grades:
            if grade < 0 or grade > 100:
                messagebox.showerror("Error", "Please enter grades between 0 and 100.")
                return

        # Calculate average grade
        average_grade = calculate_average(grades)

        # Get letter grade and GPA
        letter_grade, gpa = calculate_letter_grade_and_gpa(average_grade)

        # Display the result in a message box
        result_text = f"Average Grade: {average_grade:.2f}\nLetter Grade: {letter_grade}\nGPA: {gpa:.2f}"
        messagebox.showinfo("Grades Summary", result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric grades.")

# Create the main window
root = tk.Tk()
root.title("Student Grade Tracker")

# Create labels and entry widgets for each subject
tk.Label(root, text="Enter Grades for 5 Subjects").grid(row=0, column=1)

tk.Label(root, text="English:").grid(row=1, column=0)
entry_english = tk.Entry(root)
entry_english.grid(row=1, column=1)

tk.Label(root, text="Hindi:").grid(row=2, column=0)
entry_hindi = tk.Entry(root)
entry_hindi.grid(row=2, column=1)

tk.Label(root, text="Marathi:").grid(row=3, column=0)
entry_marathi = tk.Entry(root)
entry_marathi.grid(row=3, column=1)

tk.Label(root, text="Maths:").grid(row=4, column=0)
entry_maths = tk.Entry(root)
entry_maths.grid(row=4, column=1)

tk.Label(root, text="Science:").grid(row=5, column=0)
entry_science = tk.Entry(root)
entry_science.grid(row=5, column=1)

# Create a button to process the grades
btn_calculate = tk.Button(root, text="Calculate Grades", command=process_grades)
btn_calculate.grid(row=6, column=1)

# Start the Tkinter main loop
root.mainloop()
