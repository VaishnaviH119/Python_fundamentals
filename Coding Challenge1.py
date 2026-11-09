# Student Marks Analyzer

marks = []      # Empty List

for i in range(5):
    m = int(input("Enter Marks : "))
    marks.append(m)

def average(marks):
    return sum(marks) / len(marks)

for m in marks:
    if m >= 40:
        print(m, "Pass")
    else:
        print(m, "Fail")

print("Average:", average(marks))
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))