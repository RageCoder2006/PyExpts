# Grade Sorter App
# Assumptions: max marks are 100, there are 5 subjects only, number grade to letter grade range

m1 = float(input("Enter Marks in subject1: "))
m2 = float(input("Enter Marks in subject2: "))
m3 = float(input("Enter Marks in subject3: "))
m4 = float(input("Enter Marks in subject4: "))
m5 = float(input("Enter Marks in subject5: "))

lst = [m1, m2, m3, m4, m5]
lst.sort(reverse=True)

avg = (m1 + m2 + m3 + m4 + m5) / 5

if avg <= 100 and avg > 80:
    grade = "A"
elif avg <= 80 and avg > 70:
    grade = "B"
elif avg <= 70 and avg > 60:
    grade = "C"
elif avg <= 60 and avg > 50:
    grade = "D"
elif avg <= 50 and avg > 40:
    grade = "E"
elif avg <= 40:
    grade = "FAIL"
print("================================RESULT================================")
print(f"Sorted Marks in Descending order: {lst}")
print(f"Average Marks: {avg}")
print(f"Grade: {grade}")
