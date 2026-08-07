# DESCRIPTION: Retrieving data from a text file and encoding them so that they can be used safely in other 
# applications.

# cd ch10_encoding_encryption_hashing
# cd decoding

# Options: data01.txt , data02.txt , data03.txt

import base64

def main():
    encode_data()

def encode_data():

    # Open file

    user_file = input("File name? ")

    # if user_file == 'data01.txt':
    #     data01 = open('data01.txt', 'r')
    #     data01.read()
    # elif user_file == 'data02.txt':
    #     data02 = open('data01.txt', 'r')
    #     data02.read()
    # else: 
    #     user_file == 'data03.txt'
    #     data03 = open('data01.txt', 'r')
    #     data03.read()
    
    with open(user_file, 'r') as file:
        file_content = file.read()

    # Get data

    content_bytes = file_content.encode('ascii')
    base64_bytes = base64.b64encode(content_bytes)
    
    # Output encoded data
    print(base64_bytes)
   


main()