Introduction:

This program reads student marks from a file, calculates overall scores, assigns grades, sorts the results, and displays grade statistics using NumPy.

import numpy as np
import os

# Print the current working directory
print("Current Directory:", os.getcwd())


# FUNCTION: Read student data
def read_student_data(filename):
    try:
        # Load CSV data (expected format: reg_no, exam, coursework)
        data = np.genfromtxt(
            filename, delimiter=',', dtype=None, encoding=None,
            names=['reg_no', 'exam', 'coursework'], skip_header=1
        )
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# FUNCTION: Compute overall marks
def compute_overall_marks(data, exam_weight=0.6, coursework_weight=0.4):
    try:
        # Weighted sum: 60% exam + 40% coursework
        overall = data['exam'] * exam_weight + data['coursework'] * coursework_weight
        return overall
    except Exception as e:
        print(f"Error computing overall marks: {e}")
        return np.zeros(len(data))


# FUNCTION: Assign grades
def assign_grades(marks):
    try:
        grades = np.empty(len(marks), dtype='<U2')  # Grade array

        # Grade rules
        for i, m in enumerate(marks):
            if m >= 90:
                grades[i] = 'A+'
            elif m >= 80:
                grades[i] = 'A'
            elif m >= 70:
                grades[i] = 'B+'
            elif m >= 60:
                grades[i] = 'B'
            elif m >= 50:
                grades[i] = 'C'
            elif m >= 40:
                grades[i] = 'D'
            else:
                grades[i] = 'F'
        return grades

    except Exception as e:
        print(f"Error in grade assignment: {e}")
        return np.full(len(marks), 'F')  # Default grades


# FUNCTION: Create final structured array
def create_structured_array(data, overall, grades):
    # Create a structured NumPy array with required fields
    structured = np.zeros(
        len(data),
        dtype=[('reg_no', 'U20'), ('exam', 'f4'),
               ('coursework', 'f4'), ('overall', 'f4'), ('grade', 'U2')]
    )

    # Fill the structure fields
    structured['reg_no'] = data['reg_no']
    structured['exam'] = data['exam']
    structured['coursework'] = data['coursework']
    structured['overall'] = overall
    structured['grade'] = grades

    return structured


# FUNCTION: Sort students by overall marks
def sort_by_overall(structured):
    # Sort in descending order
    return np.sort(structured, order='overall')[::-1]


# FUNCTION: Write output to CSV
def write_output(filename, structured):
    try:
        # Save results to CSV file
        np.savetxt(
            filename, structured,
            fmt='%s,%.2f,%.2f,%.2f,%s', delimiter=',',
            header='RegNo,Exam,Coursework,Overall,Grade',
            comments=''
        )
        print(f"Results written to {filename}")

    except Exception as e:
        print(f"Error writing file: {e}")


# FUNCTION: Display grade statistics
def display_stats(grades):
    unique, counts = np.unique(grades, return_counts=True)
    print("Grade Statistics:")
    for u, c in zip(unique, counts):
        print(f"{u}: {c}")



# MAIN FUNCTION
def main():
    input_file = 'C:"C:\Users\abhis\OneDrive\Desktop\AbhistaReddy_PythonAssignment\student_marks.csv"'
    output_file = 'student_results.csv'

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Input file {input_file} does not exist.")
        return

    # Read the CSV data
    data = read_student_data(input_file)
    if data is None:
        print("No data to process.")
        return

    # Process all steps
    overall = compute_overall_marks(data)
    grades = assign_grades(overall)
    structured = create_structured_array(data, overall, grades)
    structured_sorted = sort_by_overall(structured)

    # Write results
    write_output(output_file, structured_sorted)

    # Show statistics
    display_stats(structured_sorted['grade'])


# Run the program
main()

Conclusion:

The program processes student data accurately and automatically, providing grades, sorted results, and useful statistics efficiently.