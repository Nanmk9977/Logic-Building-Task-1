marks = [45, 78, 90, 33, 60]  # List of student marks

pass_count = 0
fail_count = 0

passing_marks = 50  # Minimum marks required to pass

# Checking each student's marks
for score in marks:
    if score >= passing_marks:
        pass_count += 1
    else:
        fail_count += 1

# Printing results
print("Student Result Analysis")
print(" ")
print("Total no of Students :", len(marks))
print("No of Students Passed :", pass_count)
print("No of Students Failed :", fail_count)
