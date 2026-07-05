# DESCRIPTION: A program that converts number grades into letter

print("===== Grade Converter =====")
grade = int(input("Enter a numerical grade (1-100): "))

if 0 <= grade < 65:
    print("F")
elif 65 <= grade < 70:
    print("D")
elif 70 <= grade < 80:
    print("C")
elif 80 <= grade < 90:
    print("B")
elif 90 <= grade <= 100:
    print("A")
elif 100 <= grade:
    print("A+")
else:
    print("F")    # This allows negatives to be calucated as F