# DESCRIPTION:  Making a phishing email detector

response = input("Enter the email subject line: ")
ogresponse = response   # This so the Analyzed subject comes out as "OG" input and not lowercase letters
response = response.lower() # Detects lower case letters

print()
print("SECURITY ASSESSMENT:")

highrisk = ("urgent", "immediate action required", "account suspended", "verify account", "urgent request for bank transfer", "URGENT REQUEST")
mediumrisk = ("win", "free", "congratulations", "claim your prize")
lowrisk = ("password reset",)

if any(keyword in response for keyword in highrisk):
    print("HIGH RISK: Possible phishing attempt.")
    print("------------------------")
    print(f"Analyzed subject: \"{ogresponse}\"")
elif any(keyword in response for keyword in mediumrisk):
    print("MEDIUM RISK: Suspicious offer detected.")
    print("------------------------")
    print(f"Analyzed subject: \"{ogresponse}\" ")
elif any(keyword in response for keyword in lowrisk):
    print("LOW RISK: Verify legitimacy with sender.")
    print("------------------------")
    print(f"Analyzed subject: \"{ogresponse}\" ")
else:
    print("No phishing indicators detected.")
    print("------------------------")
    print(f"Analyzed subject: \"{ogresponse}\" ")