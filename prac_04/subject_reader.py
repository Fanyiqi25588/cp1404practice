FILENAME = "subject_data.txt"
def main():
    subjects = load_data()
    display_subject_details(subjects)

def load_data():
    subject_data = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_data.append(parts)
    return subject_data

def display_subject_details(subjects):
    for subject in subjects:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()
