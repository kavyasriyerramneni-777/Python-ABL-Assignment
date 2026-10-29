

# University Scholarship Allocation System

applicants = []

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 40
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

num = int(input("Enter number of applicants: "))

for i in range(num):
    print(f"\nEnter details of Applicant {i + 1}")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    subjects = int(input("Enter number of subjects: "))
    marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / subjects

    # Check eligibility criteria
    eligible = (
        aggregate >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARKS for mark in marks)
        and attendance >= MIN_ATTENDANCE
        and income <= MAX_INCOME
    )

    if eligible:
        applicants.append({
            "name": name,
            "roll_no": roll_no,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Rank eligible applicants
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Roll number in ascending order

applicants.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["roll_no"]
    )
)

# Display results
print("\n========== SCHOLARSHIP RESULTS ==========")

if not applicants:
    print("No eligible applicants found.")
else:
    print("\nEligible Students - Ranked List")
    print("-" * 75)
    print(f"{'Rank':<6}{'Name':<18}{'Roll No':<12}"
          f"{'Aggregate':<12}{'Attendance':<13}{'Income':<12}")
    print("-" * 75)

    for rank, student in enumerate(applicants, start=1):
        print(
            f"{rank:<6}"
            f"{student['name']:<18}"
            f"{student['roll_no']:<12}"
            f"{student['aggregate']:<12.2f}"
            f"{student['attendance']:<13.2f}"
            f"{student['income']:<12.2f}"
        )

print("\nScholarship allocation process completed.")
