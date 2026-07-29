# DESCRIPTION: Checking if what user typed is a website on approve.txt or deny.txt, if website is not on approve.txt
# or deny.txt, website input is sent to review. All entries are logged with timestamps

# Websites in txt files for input:
#   approve.txt: www.google.com, www.yandex.com, www.safewebsite.com
#   deny.txt: www.malware.com, www.scam.com, www.freemoney.com

# I edited code for directory paths to txt, all code commented out can be used with "cd ch09_files_and_folders" 

import os
import datetime

# Grabbing folder where files are located
directory = os.path.dirname(os.path.abspath(__file__))

# Building paths to txt files for github
approve_path = os.path.join(directory, "approve.txt")
deny_path = os.path.join(directory, "deny.txt")
review_path = os.path.join(directory, "review.txt")
log_path = os.path.join(directory, "log.txt")

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Turn deny.txt and approve.txt into lists 
# approve_urls = open('approve.txt', 'r')
# approve_list = approve_urls.readlines()

# deny_urls = open('deny.txt', 'r')
# denied_list = deny_urls.readlines()

with open(approve_path, 'r') as approve_urls:
    approve_list = approve_urls.readlines()

with open(deny_path, 'r') as deny_urls:
    denied_list = deny_urls.readlines()

# Ask user for a URL 
user_url = input("Enter a URL to access: ")
print("")

# Check if URL is in the approve.txt list or deny.txt list if not copy to review.txt
if user_url in approve_list:
       print("ACCESS GRANTED")
       print("--------------------------------------------------")
       print(f"       CONTENT FROM: {user_url}")
       print("--------------------------------------------------")
       print("This website has been verified as safe by your organization.\nFeel free to browse this content for business or educational purposes.\nRemember to follow the organization's acceptable use policy.")
       print("--------------------------------------------------")
elif user_url in denied_list:
       print("ACCESS DENIED")
       print("--------------------------------------------------")
       print(f"       BLOCKED URL: {user_url}")
       print("--------------------------------------------------")
       print("This website has been blocked by your organization's web filter.\nReason: This URL is on the deny list.\nIf you believe this is an error, please contact IT support.")
       print("--------------------------------------------------")
else: 
    #    reviewfile = open('review.txt', 'a')
    #    reviewfile.write(user_url)
    #    reviewfile.close

    with open(review_path, 'a') as reviewfile:
        reviewfile.write(user_url + "\n")

    ("URL UNDER REVIEW")
    print("--------------------------------------------------")
    print(f"       PENDING REVIEW: {user_url}")
    print("--------------------------------------------------")
    print("This website is not on the approve or deny lists.\nIt has been submitted for review by the security team.\nAccess is currently restricted until review is complete.\nPlease check back later or contact IT if urgent access is needed.")
    print("--------------------------------------------------\n")
    print("URL has been added to review.txt for security team review.")

# Log request with datetime
# logfile = open('log.txt', 'a')
# logfile.write(timestamp)
# logfile.close()
with open(log_path, 'a') as logfile:
    logfile.write(timestamp + "\n")

print("")
print("This access attempt has been logged to log.txt")

# DEBUG 
# logfile = open('log.txt', 'r')
# logfile_info = logfile.readlines()
# print(logfile_info)

# reviewfile = open('review.txt', 'r')
# reviewfile_info = reviewfile.readlines()
# print(reviewfile_info)