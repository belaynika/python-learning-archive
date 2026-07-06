# DECRIPTION: a program that sums up the failed login attempts over the week
# anti-brute force program 

print("Please enter failed login attempts")
print("==================================")
print(" ")

mon = int(input("  Monday:    "))
tue = int(input("  Tuesday:   "))
wed = int(input("  Wednesday: "))
thur = int(input("  Thursday:  "))
fri = int(input("  Friday:    "))

numbers = [mon, tue, wed, thur, fri]
total = sum(numbers)

print(" ")
print(" ")
print("===== FAILED LOGIN ATTEMPTS ANALYZER =====")
print(" ")
print(f"Total failed login attempts for the week: {total}")
print(" ")

if total > 100: 
  print("SECURITY ALERT: Weekly threshold of 100 attempts has been exceeded!")
  print("Recommendation: Investigate for potential brute force attacks.")
else:
    print("Everything seems normal. It's quiet. Too quiet.")
    print("Recommendation: Continue routine monitoring.")