#TASK_2 : -  CSV Data Handler:- Read and write CSV files with student data, calculate averages

import csv 
# class CsvReader:

# Function to read a CSV file and return a list of dictionaries (each representing a student)
def read_csv(filename):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary contains student data with subjects and marks.
    """
    with open(filename, mode='r') as file:
        # DictReader automatically uses the first row as field names
        reader = csv.DictReader(file)
        data = [row for row in reader]  # Read each row into a list
    return data
# Function to write student data (including averages) to a new CSV file
def write_csv(filename, data, fieldnames):
    """
    Writes a list of dictionaries to a CSV file using the given field names.
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # Set up writer with column names
        writer.writeheader()  # Write the header row (field names)
        writer.writerows(data)  # Write all student rows
# Function to calculate average marks for each student
def calculate_student_averages(data):
    """
    Calculates the average marks for each student and adds it to their dictionary.
    """
    for student in data:
        # Extract all subject scores (excluding the 'Name' field)
        scores = [float(student[subject]) for subject in student if subject != 'Name']
        # Calculate average and round to 2 decimal places
        student['Average'] = round(sum(scores) / len(scores), 2)
    return data  # Return updated list with averages included
# Function to calculate average marks per subject
def calculate_subject_averages(data):
    """
    Calculates and returns the average marks for each subject.
    """
    if not data:
        return {}  # Return empty dictionary if no student data
    # Get list of subject names (excluding 'Name')
    subjects = [subject for subject in data[0] if subject != 'Name']
    averages = {}  # Dictionary to hold subject averages
    for subject in subjects:
        # Sum the marks for each subject across all students
        total = sum(float(student[subject]) for student in data)
        # Calculate average and store in the dictionary
        averages[subject] = round(total / len(data), 2)
    return averages  # Return dictionary of subject averages
# -------- Main Program --------
if __name__ == "__main__":
    # Input and output CSV file names
    input_file = 'sdata.csv'
    output_file = 'students_with_averages.csv'
    # Step 1: Read student data from the input file
    students = read_csv(input_file)
    # Step 2: Calculate individual student averages
    students_with_avg = calculate_student_averages(students)
    # Step 3: Get list of field names including the new 'Average' column
    fieldnames = list(students_with_avg[0].keys())
    # Step 4: Write updated student data to a new CSV file
    write_csv(output_file, students_with_avg, fieldnames)
    # Step 5: Calculate and print subject-wise average marks
    subject_averages = calculate_subject_averages(students)
    print("📊 Subject Averages:")
    for subject, avg in subject_averages.items():
        print(f"{subject}: {avg}")
