# Function to calculate the grade based on the test result
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Function to provide comments based on the grade
def provide_comments(grade):
    if grade == "A":
        return "Excellent work!"
    elif grade == "B":
        return "Good job!"
    elif grade == "C":
        return "Keep up the effort!"
    elif grade == "D":
        return "You can do better!"
    else:
        return "You need to improve!"

# Number of students
num_students = int(input("Enter the number of students: "))

# Dictionary to store student names and test results
students = {}

# Loop to get test results for each student
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    score = float(input(f"Enter the test result for {name}: "))
    grade = calculate_grade(score)
    comment = provide_comments(grade)
    students[name] = {"Score": score, "Grade": grade, "Comment": comment}

# Sorting the students based on their scores
sorted_students = sorted(students.items(), key=lambda x: x[1]["Score"], reverse=True)

# Displaying the ranks and comments for each student
print("Rank\tName\t\tScore\tGrade\tComment")
for rank, (name, details) in enumerate(sorted_students, start=1):
    print(f"{rank}\t{name}\t\t{details['Score']}\t{details['Grade']}\t{details['Comment']}")
